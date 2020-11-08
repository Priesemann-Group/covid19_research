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
void parameter_swipe_ld_dates();
int main();
void stable_model_to_tipping_point();
}