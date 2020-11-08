#include "solver.h"

Solver::Solver(Model *_model){
	model = _model;
}
Solver::~Solver(){
	dt = 0.1;
	data.clear();
};

void Solver::run(SV initial, double t_max){
	/* Runs model and populates the data vectors!
	
	Parameters
	----------
	initial: 
		Initial State array
	t_max:
		At wich time t to stop the simulation
	*/

	
	// Clear old data
	data.clear();
	model->clear();

	// Initial value
	data.push_back(0.0,initial);
	model->time.push_back(0.0);
	model->I_H_tau.push_back(initial[4]);
	model->I_Hs_tau.push_back(initial[5]);
	//memory alloc for next array
	SV next = initial;

	// Do RK4 steps till t_max
	double t = 0.0;
	while(t<t_max){
		next = runge_kutta4(dt,t,next);
		data.push_back(t,next);
		//Add a dirty hack to help calculate N_traced remove if other model
		model->time.push_back(t);
		model->I_H_tau.push_back(next[4]);
		model->I_Hs_tau.push_back(next[5]);
		t=t+dt;
	}
}

data_struct Solver::get_data(){
	return data;
};


SV Solver::runge_kutta23(double dt, double t, SV _SV){
	/* Performs a runge kutta timestep with the model.dgl function
	Matlab solver
	https://www-m2.ma.tum.de/foswiki/pub/M2/Allgemeines/NODE/folien_Runge_Kutta.pdf
	Parameter
	---------
	dt:
		timestep length
	t:
		time for timestep start
	SV:
		state vector
	*/
	SV k_1;
	SV k_2;
	SV k_3;
	SV k_4;
	SV k_2_SV;
	SV k_3_SV;	
	//Calc first step
	k_1 = model->dgl(t,_SV);

	//Prep new state vector and calc second step
	for (long unsigned int i = 0; i < _SV.size(); ++i)
	{
		k_2_SV[i] = _SV[i] + k_1[i] * dt / 2.0;
	}
	k_2 = model->dgl(t + dt / 2.0, k_2_SV);
	//Prep new state vector and calc third step
	for (long unsigned int i = 0; i < _SV.size(); ++i)
	{
		k_3_SV[i] = _SV[i] + k_2[i] * dt * 3.0 / 4.0;
	}
	k_3 = model->dgl(t + dt * 3.0 / 4.0, k_3_SV);

	//CALC return value
	SV y,z;
	for (long unsigned int i = 0; i < _SV.size(); ++i)
	{
		y[i] = _SV[i] + 2.0 / 9.0 * dt / k_1[i] + 1.0/ 3.0 * dt / k_2[i] + 4.0/9.0* dt* k_3[i];
	}	
	k_4 = model->dgl(t + dt , y);
	for (long unsigned int i = 0; i < _SV.size(); ++i)
	{
		z[i] = _SV[i] + 7.0 / 24.0 * dt / k_1[i] + 1.0 / 4.0 * dt / k_2[i] + 1.0/3.0* dt* k_3[i] + 1.0/8.0 * dt * k_4[i];
	}	


	this->dt = get_next_timestep_adaptive(y,z);

	return y;
}

double Solver::get_next_timestep_adaptive(SV &y, SV &z){
	//Update next timestep dt
	double tau = 0.0;
	for (long unsigned int i = 0; i < y.size(); ++i)
	{
		tau += (z[i]-y[i])*(z[i]-y[i]);
	}
	tau = tau/(dt*0.1); //q_h 
	double alpha = max(0.2,pow(tau,-1./3.));
	alpha = min(1.5,alpha);
	return min(1.0,max(0.01,0.85*alpha*dt));
}


SV Solver::runge_kutta4(double dt, double t, SV _SV){
	/* Performs a runge kutta timestep with the model.dgl function
	Parameter
	---------
	dt:
		timestep length
	t:
		time for timestep start
	SV:
		state vector
	*/
	SV k_1;
	SV k_2;
	SV k_3;
	SV k_4;
	SV k_2_SV;
	SV k_3_SV;
	SV k_4_SV;	
	//Calc first step
	k_1 = model->dgl(t,_SV);

	//Prep new state vector and calc second step
	for (long unsigned int i = 0; i < _SV.size(); ++i)
	{
		k_2_SV[i] = _SV[i] + k_1[i] * dt / 2.0;
	}
	k_2 = model->dgl(t + dt / 2.0, k_2_SV);
	//Prep new state vector and calc third step
	for (long unsigned int i = 0; i < _SV.size(); ++i)
	{
		k_3_SV[i] = _SV[i] + k_2[i] * dt / 2.0;
	}
	k_3 = model->dgl(t + dt / 2.0, k_3_SV);
	//Prep new state vector and calc forth step
	for (long unsigned int i = 0; i < _SV.size(); ++i)
	{
		k_4_SV[i] = _SV[i] + k_3[i] * dt;
	}
	k_4 = model->dgl(t + dt, k_4_SV);

	//CALC return value
	SV next_SV;
	for (long unsigned int i = 0; i < _SV.size(); ++i)
	{
		next_SV[i] = _SV[i] + dt / 6.0 * (k_1[i] + 2.0 *  k_2[i] + 2.0 * k_3[i] + k_4[i]);
	}	


	return next_SV;
}
