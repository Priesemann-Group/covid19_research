// ---------------------------------------------------------------------------- //
// Design Choices:
//	We transfer the statevector as std::array
//	And save a list of state vectors via std::vector
// 
// ---------------------------------------------------------------------------- //
#include "scripts.h"
using namespace std;

namespace szenarios{
void parameter_swipe_ld_dates(){
	SV initials = {
		//Susceptible pool  S
		1e6 - 4*200.0,

		//Exposed pool (quarantined)  E_Q
		200.0,

		//Exposed pool (hidden)				E_H
		200.0,

		//Infectious (quarantined)		I_Q 	
		200.0,

		//Infectious (hidden)					I_H
		200.0,

		//Infectious (hidden, symptomatic) I_Hs
		(1.0-0.32)*200.0, 

		//Recovered  R
		0, 		
	};

	double t_max = 400;

	Model main_model(initials);
	std::vector<Model> models;

	//Pushback new models
	double date = 20.0;
	double date_max = 380;
	while(date<date_max){
		Model model = main_model;

		//Set cp for lockdown
		model.k = TimeDependentParameter(0.8);
		model.k.add_change(
			date+7./2.0,       //center of cp
			7.,                //length of cp
			0.25   //value after cp
		);
		model.k.add_change(
			date+7./2.0 + 4.*7.0,       //center of cp
			7.,                				//length of cp
			0.55   										//value after cp
		);


		//Setup influx cp
		double I_0 = 0.1;
		main_model.Phi = TimeDependentParameter(I_0);
		main_model.Phi.add_change(
			90.0+7./2.0,
			7.0,
			I_0*0.1
		);
		main_model.Phi.add_change(
			90.0+7./2.0 + 7.0*4.0,
			7.0,
			I_0
		);
		model.name = to_string(date);

		//Push model to list
		models.push_back(model);

		date = date + 1.0;
	}


	// Solver for each model
	// We run the models in parallel this gets us a CRAZY speedup
	// 400 models parallel takes like 2 mins 
 	for_each(
    execution::par_unseq,
    models.begin(),models.end(),
    [initials,t_max](Model &model){
     // c++17 feature
		Solver solver(&model);
		solver.run(initials,t_max);

		//Get data 
		data_struct data;
		data = solver.get_data();
		save_to_file(data, model,"./data/variate_ld_dates/"+model.name+".csv");
	});
}

void stable_model_to_tipping_point(){
	//Create stable model

	SV initials = {
		//Susceptible pool  S
		1e6 - 4*10.0,

		//Exposed pool (quarantined)  E_Q
		10.0,

		//Exposed pool (hidden)				E_H
		10.0,

		//Infectious (quarantined)		I_Q 	
		10.0,

		//Infectious (hidden)					I_H
		10.0,

		//Infectious (hidden, symptomatic) I_Hs
		(1.0-0.32)*10.0, 

		//Recovered  R
		0, 		
	};

	double t_max = 300;
	Model main_model(initials);
	
	main_model.Phi = TimeDependentParameter(0.1);


	std::vector<Model> models;
	//Add change to behaviour
	
	double capacity = 20.0;
	while(capacity < 5500.){
		Model new_mod = main_model;
		new_mod.name = to_string(capacity);
		new_mod.N_test_max = capacity;
		models.push_back(new_mod);
		capacity += 5.0;
	}



 	for_each(
    execution::par_unseq,
    models.begin(),models.end(),
    [initials,t_max](Model &model){
     // c++17 feature
		Solver solver(&model);
		solver.run(initials,t_max);

		//Get data 
		data_struct data;
		data = solver.get_data();
		save_to_file(data, model,"./data/tipping_point/"+model.name+".csv");
	});
}


int main()
{
	// First we create an instance of our model defined in model.h


	return 0;
}

}