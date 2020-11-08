#pragma once
#include <vector>
#include <cmath>
#include <fstream>
#include <string>
#include "model.h"
using namespace std;

double interpolate(vector<double> &xData, vector<double> &yData, double x, bool extrapolate);
double logistics(double t, double center, double length, double change);
double gaussian_peak(double t, double mean, double variance, double change);


std::vector<double> get_new_cases(data_struct &data, Model &model);
vector<double> get_new_cases_obs(data_struct &data, Model &model);
void save_to_file(data_struct &data, Model &model,string fpath);