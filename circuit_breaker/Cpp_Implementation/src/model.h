// ---------------------------------------------------------------------------- //
// Class for the model (dgl)
// Contains every non state vector initial values and other functions
// of the model
// ---------------------------------------------------------------------------- //

#pragma once
#include <vector>
#include <array>
#include <string>
#include <iostream>
#include "timeDependentParameter.h"
using namespace std;

//Our state vector has size one atm
typedef array<double, 7> SV;

// ---------------------------------------------------------------------------- //
// Main model class
// ---------------------------------------------------------------------------- //
class Model
{
public:
	Model();
	Model(SV initials);
	~Model();
	SV dgl(double t, SV state);
	void clear(); //Clear the time hs h data

	// Name var can be used for file saveing ...
	string name;

	// Parameters first order (time independent)
	double M;  						//Population size gets set on init

	double gamma 					//Recovery/removal rate
		= 0.10; 	  
	double xi		 					//Asymptomatic ratio
		= 0.32;
  double nu  	 					//Registered contacts (quarantined)
  	= 0.075;
	double lambda_r 			//Random testing rate
		= 0.0;
	double lambda_r_prime //Reduced random testing rate
		= 0.0;
	double lambda_s 			//Symptom driven testing rate
		= 0.25;
	double lambda_s_prime //symptom-driven testing rate in reduced capacity
		= 0.10;	
	double eta 						//Tracing efficiency
		= 0.66;
	double tau 						//Contact tracing delay
		= 2.0;
	double N_test_max 		//Maximal tracing capacity
		= 50.0;
	double epsilon 				//Leak factor (quarantined)
		= 0.05;
	double rho   					//Exposed-to-infectious rate
		= 0.25;
	double phi 						//ratio 
		= 0.38;
	double R_0						//Basic reproduction number
		= 3.3;

	SV init;

	// Parameters second order (time dependent)
	// small class which allows easy modeling
	TimeDependentParameter k{0.8}; // Contacts
	TimeDependentParameter Phi{0.1}; // Influx


	// Parameters thrid order (hard coded special behaviour or dependence
	// on other parameters)
	double chi_tau();
	double chi_sr();
	double chi_r();
	double I_H_max();
	double I_Hs_max();
	double N_test(double I_H, double I_Hs);
	double N_test_S(double I_Hs);
	double N_traced(double t);

	// Data vectors to save a part of the last calculations
	std::vector<double> time;
	std::vector<double> I_H_tau;
	std::vector<double> I_Hs_tau;
private:
};


// ---------------------------------------------------------------------------- //
// Data Struct for saving the timeseries of the state vector
// ---------------------------------------------------------------------------- //
struct data_struct{
	vector<double> time;
	vector<SV> system;

	void clear(){
		time.clear();
		system.clear();
	}

	void push_back(double _time, SV _data){
		time.push_back(_time);
		system.push_back(_data);
	}
};
