#pragma once
#include <iostream>
#include <vector>
#include <array>
#include <string>
#include "model.h"
#include "solver.h"
#include "timeDependentParameter.h"
#include "utils.h"
#include <execution>

namespace szenarios{

int main();
void stable_model_to_tipping_point();

void lockdown_swipe(
	double start_strength, double end_strength, double inc_strength,
	double start_date 	 , double end_date    , double inc_date,
	double start_length  , double end_length  , double inc_length 
	);
void parameter_swipe_ld_dates();
void parameter_swipe_ld_strength();


void swipe_k_phi(
	double start_k,   double end_k, double inc_k,
	double start_Phi, double end_Phi, double inc_Phi);

void influx_event_from_equilibrium(
	double start_k,   double end_k, double inc_k,
	double start_Phi, double end_Phi, double inc_Phi);


void swipe_equilibrium(
	double start_k,   double end_k, double inc_k,
	double start_Phi, double end_Phi, double inc_Phi);
}