	// First we create an instance of our model defined in model.h
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

	// Model has to be initialised with the initial values
	Model main_model(initials);

	//Contact k
	main_model.k = TimeDependentParameter(0.8);
	main_model.k.add_change(
		90.0+7./2.0,       //center of cp
		7.,                //length of cp
		0.25   //value after cp
		);

	main_model.k.add_change(
		90.0+7./2.0 + 4.*7.0,       //center of cp
		7.,                				//length of cp
		0.55   										//value after cp
		);

	//Influx Phi
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

	//Different models
	Model mod_a = main_model;
	mod_a.lambda_s_prime = 0.25;
	mod_a.lambda_s = 0.25;

	Model mod_b = main_model;
	mod_b.lambda_s = 0.25;
	mod_b.lambda_s_prime = 0.10;

	//Than create the initial state and run the solver
	double t_max = 300;

	// Next we iterate over all models and save the data
	Solver solver_a(&mod_a);
	//Run solver
	solver_a.run(initials,t_max);
	//Get data 
	data_struct data_a;
	data_a = solver_a.get_data();
	//Save to file
	save_to_file(data_a, mod_a,"data/lambda_equals_lambda_prime.csv");
	int ii = 0;
	for (double t = 0; t < t_max; t=t+0.1)
	{
		cout << t << "\t" << mod_a.N_traced(t) << "\t"<< mod_a.time[ii] <<std::endl;
		ii++;
	}
	// Next we iterate over all models and save the data
	Solver solver_b(&mod_b);
	//Run solver
	solver_b.run(initials,t_max);
	//Get data 
	data_struct data_b;
	data_b = solver_b.get_data();
	//Save to file
	save_to_file(data_b, mod_b,"data/lambda_not_equals_lambda_prime.csv");