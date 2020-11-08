#include "timeDependentParameter.h"
#include <cmath>
#include "utils.h"
// ---------------------------------------------------------------------------- //
// Class Constructor and main entry point
// ---------------------------------------------------------------------------- //
TimeDependentParameter::TimeDependentParameter(){
}

TimeDependentParameter::TimeDependentParameter(double _initial_value){
	initial_value = _initial_value;
}

TimeDependentParameter::~TimeDependentParameter(){
	change_points.clear();
}

//Add main entry point to call the class and get a value
//at time t.
double TimeDependentParameter::operator()(double t){

	//Get value at time t
	double return_value = 0.0;

	// ---------------------------------------------------------------------------- //
	// Addition of different functions
	// ---------------------------------------------------------------------------- //
	// First calculate logistics
	for (long unsigned int i = 0; i < change_points.size(); ++i)
	{
		//Calculate change from last value
		double change;
		if (i == 0)
		{
			change = change_points[i].next_value - initial_value;
		}
		else{
			change = change_points[i].next_value - change_points[i-1].next_value;
		}

		// Add all logistic functions
		return_value += logistics(t,
			change_points[i].center,
			change_points[i].length,
			change
			);
	}

	//Second calculate gaussian peaks
	for (long unsigned int i = 0; i < input_events.size(); ++i)
	{
		return_value += gaussian_peak(t,
			input_events[i].mean,
			input_events[i].variance,
			input_events[i].change
			);
	}

	return return_value + initial_value;

};

// ---------------------------------------------------------------------------- //
// Add to internal TimeDependentParameter function
// ---------------------------------------------------------------------------- //
// Add change points
void TimeDependentParameter::add_change(double center, double length, double next_value){
	/*
	Should be added in cronological order!

	length: length of the change
	start: start of the change point
	next_value: next value for parameter
	*/
	ChangePoint cp(center,length,next_value); 
	add_change(cp);
}

void TimeDependentParameter::add_change(ChangePoint cp){
	change_points.push_back(cp);
}


// Add input event
void TimeDependentParameter::add_inputevent(double mean, double variance, double change){
	/*
	Should be added in cronological order!

	mean: length of the change
	variance: start of the change point
	change: next value for parameter
	*/
	InputEvent in(mean,variance,change); 
	add_inputevent(in);
}

void TimeDependentParameter::add_inputevent(InputEvent in){
	input_events.push_back(in);
}


