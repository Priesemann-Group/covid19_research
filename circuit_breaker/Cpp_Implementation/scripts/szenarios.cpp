// ---------------------------------------------------------------------------- //
// Design Choices:
//	We transfer the statevector as std::array
//	And save a list of state vectors via std::vector
// 
// ---------------------------------------------------------------------------- //
#include "scripts.h"
using namespace std;
#include <sstream>
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
		model.k = TimeDependentParameter(0.75);
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



void parameter_swipe_ld_strength(){
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

	double t_max = 500;

	Model main_model(initials);
	std::vector<Model> models;

	//Pushback new models
	double date = 82.0;
	double transient = 7.0;
	double strength = 0.8;
	while(strength>0.1){
		Model model = main_model;

		//Set cp for lockdown
		model.k = TimeDependentParameter(0.8);
		if (strength<=0.6)
		{
			model.k.add_change(
				date+transient/2.0,       //center of cp
				transient,                //length of cp
				strength  //value after cp
			);
			model.k.add_change(
				date+transient/2.0 + 4.*7.0,       //center of cp
				transient,                				//length of cp
				0.6   										//value after cp
			);
		
			//Setup influx cp
			double I_0 = 0.1;
			model.Phi = TimeDependentParameter(I_0);
			model.Phi.add_change(
				date+transient/2.0,
				transient,
				I_0*0.1
			);
			model.Phi.add_change(
				date+7./2.0 + 7.0*4.0,
				7.0,
				I_0
			);
		}
		model.name = to_string(strength);

		//Push model to list
		models.push_back(model);

		strength = strength - 0.01;
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
		save_to_file(data, model,"./data/variate_ld_strength/"+model.name+".csv");
	});
}


void stable_model_to_tipping_point(){
	/*
	Does a parameter swipe of different starting values
	for the pools, and capacity of the tracing pools.
	*/



	//Create stable model
	double t_max = 400;
	
	std::vector<Model> models;

	//We variate capacity
	double capacity = 5.0;
	while(capacity < 100.){
		double I_0 = 1.0;
		while(I_0 < 10.0){
			SV initials = {
				//Susceptible pool  S
				1e6 - 4*I_0,

				//Exposed pool (quarantined)  E_Q
				I_0,

				//Exposed pool (hidden)				E_H
				I_0,

				//Infectious (quarantined)		I_Q 	
				I_0,

				//Infectious (hidden)					I_H
				I_0,

				//Infectious (hidden, symptomatic) I_Hs
				(1.0-0.32)*I_0, 

				//Recovered  R
				0, 		
			};

			Model new_mod(initials);
			new_mod.k = TimeDependentParameter(0.8);
			new_mod.N_test_max = capacity;

			new_mod.name =  to_string(capacity).substr(0, to_string(capacity).find("."))
										+"_"+
										  to_string(I_0).substr(0, to_string(I_0).find("."));
			
			models.push_back(new_mod);
			I_0++;
		}
		capacity += 1.0;
	}



 	for_each(
    execution::par_unseq,
    models.begin(),models.end(),
    [t_max](Model &model){
     // c++17 feature
		Solver solver(&model);
		solver.run(model.init,t_max);

		//Get data 
		data_struct data;
		data = solver.get_data();
		save_to_file(data, model,"./data/tipping_point/"+model.name+".csv");
	});

}




void swipe_k_phi(
	double start_k,   double end_k, double inc_k,
	double start_Phi, double end_Phi, double inc_Phi){
	/* Does a parameter swipe for k and phi but needs uncommenting
	in the model euqations*/

	SV initials_high = {
		//Susceptible pool  S
		1e6, //- 4*200.0,

		//Exposed pool (quarantined)  E_Q
		1000.0,

		//Exposed pool (hidden)				E_H
		1000.0,

		//Infectious (quarantined)		I_Q 	
		1000.0,

		//Infectious (hidden)					I_H
		1000.0,

		//Infectious (hidden, symptomatic) I_Hs
		(1.0-0.32)*1000.0, 

		//Recovered  R
		0, 		
	};
	SV initials_low = {
		//Susceptible pool  S
		1e6, //- 4*200.0,

		//Exposed pool (quarantined)  E_Q
		1.0,

		//Exposed pool (hidden)				E_H
		1.0,

		//Infectious (quarantined)		I_Q 	
		1.0,

		//Infectious (hidden)					I_H
		1.0,

		//Infectious (hidden, symptomatic) I_Hs
		(1.0-0.32)*1.0, 

		//Recovered  R
		0, 		
	};
	double t_max = 3000.0;


	std::vector<Model> models;
	for (double k = start_k; k < end_k; k = k+inc_k)
	{
		for (double Phi = start_Phi; Phi < end_Phi; Phi = Phi+inc_Phi)
		{
			//Create model
			Model new_mod_low(initials_low);

			//Set name of model
			new_mod_low.name =  convert_double_to_fixed(double(initials_low[1]),3) + "_" + convert_double_to_fixed(k, 3) + "_" +convert_double_to_fixed(Phi, 3);

			new_mod_low.k = TimeDependentParameter(k);
			new_mod_low.Phi = TimeDependentParameter(Phi);

			models.push_back(new_mod_low);

			//Create model
			/*
			Model new_mod_high(initials_high);

			//Set name of model
			new_mod_high.name =  convert_double_to_fixed(double(initials_high[1]),3) + "_" + convert_double_to_fixed(k, 3) + "_" +convert_double_to_fixed(Phi, 3);

			new_mod_high.k = TimeDependentParameter(k);
			new_mod_high.Phi = TimeDependentParameter(Phi);

			models.push_back(new_mod_high);
			*/
		}
	}


 	for_each(
    execution::par_unseq,
    models.begin(),models.end(),
    [t_max](Model &model){
     // c++17 feature
		Solver solver(&model);
		solver.run(model.init,t_max);

		//Get data 
		data_struct data;
		data = solver.get_data();


		save_to_file(data, model,"./data/variate_k_Phi/"+model.name+".csv");
	});
}



void lockdown_swipe(
	double start_strength, double end_strength, double inc_strength,
	double start_date 	 , double end_date    , double inc_date,
	double start_length  , double end_length  , double inc_length 
	){
	/*
	Does a parameter swipe for strength, date and length of ld!
	Parameters should be self explanatory.
	*/


	/*Config*/
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

	double t_max = 500.0;
	double transient = 7.0;
	double Phi_0 = 0.1;

	std::vector<Model> models;
	for (double strength = start_strength; strength < end_strength; strength=strength+inc_strength)
	{
		for (double date = start_date; date < end_date; date=date+inc_date)
		{
			for (double length = start_length; length < end_length; length=length+inc_length)
			{

				//Create model
				Model new_mod(initials);
				//Set name of model
				new_mod.name =  convert_double_to_fixed(strength, 3) + "_" +convert_double_to_fixed(date, 3) +"_"+ convert_double_to_fixed(length, 3);

				//Add Lockdown
				new_mod.k.add_change(
					date+transient/2.0,       //center of cp
					transient,                //length of cp
					strength  								//value after cp
				);
				new_mod.k.add_change(
					date+transient/2.0 + length,       //center of cp
					transient,                				//length of cp
					0.6   										//value after cp
				);
		
				new_mod.Phi = TimeDependentParameter(Phi_0);
				new_mod.Phi.add_change(
					date+transient/2.0,
					transient,
					Phi_0*0.1
				);
				new_mod.Phi.add_change(
					date+7./2.0 + length,
					7.0,
					Phi_0
				);

				//Push model to list
				models.push_back(new_mod);
			}
		}
	}

 	for_each(
    execution::par_unseq,
    models.begin(),models.end(),
    [t_max](Model &model){
     // c++17 feature
		Solver solver(&model);
		solver.run(model.init,t_max);

		//Get data 
		data_struct data;
		data = solver.get_data();


		save_to_file(data, model,"./data/variate_ld/"+model.name+".csv");
	});


}




void influx_event_from_equilibrium(
	double start_k,   double end_k, double inc_k,
	double start_Phi, double end_Phi, double inc_Phi){

	SV initials_low = {
		//Susceptible pool  S
		1e6, //- 4*200.0,

		//Exposed pool (quarantined)  E_Q
		2.0,

		//Exposed pool (hidden)				E_H
		2.0,

		//Infectious (quarantined)		I_Q 	
		2.0,

		//Infectious (hidden)					I_H
		2.0,

		//Infectious (hidden, symptomatic) I_Hs
		(1.0-0.32)*2.0, 

		//Recovered  R
		0, 		
	};
	double t_max = 3000.0;

	std::vector<Model> models;
	for (double k = start_k; k < end_k; k = k+inc_k)
	{
		for (double Phi = start_Phi; Phi < end_Phi; Phi = Phi+inc_Phi)
		{
		//Create model
		
		Model new_mod_low(initials_low);

		//Set name of model
		new_mod_low.name = convert_double_to_fixed(k, 3) +"_"+ convert_double_to_fixed(Phi, 3);
		new_mod_low.k = TimeDependentParameter(k );
		new_mod_low.Phi = TimeDependentParameter(Phi);

		//Add influx event at t = 1000; 
		new_mod_low.Phi.add_inputevent(
			2200.0, //mean
			4.0,
			100.0
			);

		models.push_back(new_mod_low);

		}
	}



	//Run
 	for_each(
    execution::par_unseq,
    models.begin(),models.end(),
    [t_max](Model &model){
     // c++17 feature
		Solver solver(&model);
		solver.run(model.init,t_max);

		//Get data 
		data_struct data;
		data = solver.get_data();


		save_to_file(data, model,"./data/eq_with_influx/"+model.name+".csv");
	});
}




void swipe_equilibrium(
	double start_k,   double end_k, double inc_k,
	double start_Phi, double end_Phi, double inc_Phi){

	SV initials_low = {
		//Susceptible pool  S
		1e6, //- 4*200.0,

		//Exposed pool (quarantined)  E_Q
		1.0,

		//Exposed pool (hidden)				E_H
		1.0,

		//Infectious (quarantined)		I_Q 	
		1.0,

		//Infectious (hidden)					I_H
		1.0,

		//Infectious (hidden, symptomatic) I_Hs
		(1.0-0.32)*1.0, 

		//Recovered  R
		0, 		
	};
	double t_max = 3000.0;


	std::vector<Model> models;
	for (double k = start_k; k < end_k; k = k+inc_k)
	{
		for (double Phi = start_Phi; Phi < end_Phi; Phi = Phi+inc_Phi)
		{
		//Create model
		
		Model new_mod_low(initials_low);

		//Set name of model
		new_mod_low.name = convert_double_to_fixed(k, 3) +"_"+ convert_double_to_fixed(Phi, 3);
		new_mod_low.k = TimeDependentParameter(k );
		new_mod_low.Phi = TimeDependentParameter(Phi);

		models.push_back(new_mod_low);

		}
	}
	//Run
 	for_each(
    execution::par_unseq,
    models.begin(),models.end(),
    [t_max](Model &model){
     // c++17 feature
		Solver solver(&model);
		solver.run(model.init,t_max);

		//Get data 
		data_struct data;
		data = solver.get_data();


		save_to_file(data, model,"./data/short_swipe/"+model.name+".csv");
	});
}




int main()
{
	// First we create an instance of our model defined in model.h


	return 0;
}

}