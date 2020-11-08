// ---------------------------------------------------------------------------- //
// Class for solving a differntial equation in different manners
// SV = type of state vector defined in model.h
// ---------------------------------------------------------------------------- //

#pragma once
#include <string>
#include <iostream>
#include <cmath>
using namespace std;
#include "model.h"

class Solver
{
// ---------------------------------------------------------------------------- //
// Methods
// ---------------------------------------------------------------------------- //
public:
	Solver(Model *_model); //Constructor
	~Solver(); //Deconstructor

	void run(SV initial, double t_max);
	void run(SV initial, double t_max, string method);
	data_struct get_data();
private:
	SV runge_kutta4(double dt, double t, SV state); //RK4
	SV runge_kutta23(double dt, double t, SV state); //RK23
	

// ---------------------------------------------------------------------------- //
// Vars
// ---------------------------------------------------------------------------- //
public:
	double dt = 1.0;

private:
	Model *model;
	data_struct data;
	double get_next_timestep_adaptive(SV &y, SV &z);
};
