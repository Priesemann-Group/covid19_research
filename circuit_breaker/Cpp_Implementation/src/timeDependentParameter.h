// ---------------------------------------------------------------------------- //
//Main time dependet variable class,
//can be overloaded to have additional functionality
//Models a continuos function in the background to allow
//adaptive runge kutta algorithms.
//
//Most time dependent paramters we look at can be modeled using logistics
//so I choose to use that in the default case.
// ---------------------------------------------------------------------------- //

#pragma once
#include <vector>
#include <iostream>

//Data class for change points
struct ChangePoint
{
	ChangePoint(double c, double l, double n){
		center = c;
		length = l;
		next_value = n;
	}
	double center;
	double length;
	double next_value;
};

struct InputEvent
{
	InputEvent(double m, double v, double c){
		mean = m;
		variance = v;
		change = c;
	}
	double mean;
	double variance;
	double change;
};



class TimeDependentParameter
{
public:

	//Constructor
	TimeDependentParameter();
	TimeDependentParameter(double _initial_value);

	//Destructor
	~TimeDependentParameter();
	
	// Make class callable at time t
	double operator()(double t);

	/*Add change points i.e logistics
											/---------------------
										 /	  									 
	------------------/
	*/ 
	void add_change(double center, double length, double next_value);
	void add_change(ChangePoint cp);

	/*Add influx i.e. Gaussian peak
										 -
										/	\	
	------------------/	 \-------------------
	*/
	void add_inputevent(double mean, double variance, double change);
	void add_inputevent(InputEvent in);
private:
	double initial_value; //Value at t=0
	std::vector<ChangePoint> change_points;
	std::vector<InputEvent> input_events;
};
