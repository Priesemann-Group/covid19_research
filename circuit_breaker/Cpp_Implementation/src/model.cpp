#include "model.h"
#include <cmath>
#include "utils.h"

Model::Model(SV initials){
	//std::cout << "Model constructor" << std::endl;
	time.push_back(0.0);
	I_H_tau.push_back(initials[4]);
	I_Hs_tau.push_back(initials[5]);

	double population = 0.0;
	for (unsigned long int i = 0; i < initials.size(); ++i)
	{
		population+=initials[i];
	}
	M = population - initials[5];

	init = initials;
}

Model::~Model() {
	//std::cout << "Model deconstructor" << std::endl;
	clear();
}

void Model::clear(){
	time.clear();
	I_H_tau.clear();
	I_Hs_tau.clear();	
}


#define S current[0]
#define E_Q current[1]
#define E_H current[2]
#define I_Q current[3]
#define I_H current[4]
#define I_Hs current[5]
#define R current[6]

SV Model::dgl(double t, SV current){
	/*
	Model equations.
	State vector entries are defined for readability.
	*/


	SV next;

	//S compartment
	/*
	next[0] =
		-gamma*k(t)*R_0*S/M*I_H   -					//hidden contagion
		gamma*(nu+epsilon)*R_0*S/M*I_Q   	- 				//traced contagion
		Phi(t)*S/M;												//external influx
	*/
	S = 1e6;
	//E_Q compartment
	next[1] = 
		nu*gamma*R_0*S/M*I_Q + 				//traced contagion
		chi_tau()*N_traced(t)   -				//contact tracing
		rho*E_Q;											//end of latency

	//E_H compartment
	next[2] = 
		gamma*S/M*(k(t)*R_0*I_H+epsilon*I_Q*R_0) -	//hidden contagion
		chi_tau()*N_traced(t)					   -	//contact tracing
		rho*E_H;
														
	//I_Q compartment
	next[3] =
		rho*E_Q - gamma*I_Q	+									//spreading dynamics
		N_test(I_H,I_Hs)  + 																//testing	
		(chi_sr()*(1.0-xi) + chi_r()*xi) * N_traced(t);	//contact tracing

	//I_H compartment
	next[4] =
		rho*E_H - gamma*I_H -           				//spreading dynamics
		N_test(I_H,I_Hs) -																	//testing
		(chi_sr()*(1.0-xi) + chi_r()*xi ) * N_traced(t) +	//contact tracing
		Phi(t)*S/M;																	//external influx

	//I_Hs compartment
	next[5] = 
		(1.0-xi)*rho*E_H - gamma*I_Hs -           			//spreading dynamics
		N_test_S(I_Hs) -																//testing	
		(1.0-xi)*(
		chi_sr()*N_traced(t)-												    //contact tracing
		Phi(t)*S/M); 																//external influx							
	
	//R compartment
	next[6] = gamma*(I_Q+I_H);
	return next;
}

// ---------------------------------------------------------------------------- //
// Parameters third order
// ---------------------------------------------------------------------------- //
double Model::chi_tau(){
	return exp(-rho*tau);
}

double Model::chi_sr(){
	if (abs(rho - (lambda_s+lambda_r)) < 1e-5){
		return rho*tau*exp(-rho*tau);
	}
	return 
		rho/((lambda_s+lambda_r)-rho)*
		(
			exp(-rho*tau)-
			exp(-tau*(lambda_s+lambda_r))
		);
}
double Model::chi_r(){
	if (abs(rho - lambda_r) < 1e-5){
		return rho*tau*exp(-rho*tau);
	}
	else{
		return rho/(lambda_r-rho)*
		(
		exp(-rho*tau)-
		exp(-tau*lambda_r)
		);
	}
}


double Model::I_H_max(){
	return N_test_max/(phi*lambda_s+lambda_r);
}
double Model::I_Hs_max(){
	return phi*N_test_max/(phi*lambda_s+lambda_r);
}


double Model::N_test(double _I_H, double _I_Hs){
	return 
		lambda_r*min(_I_H,I_H_max()) + lambda_r_prime*max(0.0,_I_H - I_H_max())
		+ lambda_s*min(_I_Hs,I_Hs_max()) + lambda_s_prime*max(0.0,_I_Hs - I_Hs_max());
}

double Model::N_test_S(double _I_Hs){
	return 
		lambda_r*min(_I_Hs,I_Hs_max()) + lambda_r_prime*max(0.0,_I_Hs - I_Hs_max())
		+ lambda_s*min(_I_Hs,I_Hs_max()) + lambda_s_prime*max(0.0,_I_Hs - I_Hs_max());
}


double Model::N_traced(double t){
	double _I_H, _I_Hs;
	if ((t-tau) > time[0])
	{
		_I_Hs = interpolate(time, I_Hs_tau, t-tau, true);
		_I_H = interpolate(time, I_H_tau, t-tau, true);
		
	} else{
		_I_Hs = I_Hs_tau[0];
		_I_H = I_H_tau[0];
	}


	double t_s = gamma/(gamma+lambda_s+lambda_r);
	double t_r = gamma/(gamma+lambda_r);

	
	if (N_test(_I_H,_I_Hs) <= N_test_max)
	{
		return eta*k(t-tau)*R_0*(_I_H*t_r*lambda_r+_I_Hs*(t_s*lambda_s+(t_s-t_r)*lambda_r));
	}
	else{
		double lambda_eq = (lambda_r*(1.0-phi)*t_r+phi*lambda_s*t_s)/(lambda_r+phi*lambda_s);
		return eta*k(t-tau)*R_0*N_test_max*lambda_eq;
	}
}
