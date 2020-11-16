#include <iostream>
#include <string>
#include "scripts/scripts.h"
using namespace std;


int main(int argc, char const *argv[])
{
	// ---------------------------------------------------------------------------- //
	// # Selector for multiple answers
	// Used to run different functions in the scripts folder
	// ---------------------------------------------------------------------------- //
  

  //Output options
  start:
  std::cout << "1\t\t Parameter swipe lockdown date\n"; 
  std::cout << "2\t\t Stable model into tipping point\n";
  std::cout << "3\t\t Parameter swipe ld full\n";
  std::cout << "4\t\t Parameter swipe k phi\n";
  std:: cout << "5\t\t Influx event from equilibrium"<<endl;
  int x;
	cin >> x;

	switch(x){
		case 1:
			szenarios::parameter_swipe_ld_dates();
			return 0;
		case 2:
			szenarios::stable_model_to_tipping_point();
			return 0;
		case 3:
			szenarios::lockdown_swipe(
				0.05,0.6,0.05, //strength
				82.0,140.0,1.0, //date
				7.0,6*7.0,1.0 //length
				);
			return 0;
		case 4:
			szenarios::swipe_k_phi(
				0.05,0.8,0.005, //k
				0.1,10.5,0.2 //Phi
				);
			return 0;
		case 5:
			szenarios::influx_event_from_equilibrium(
				0.1,0.8,0.001, //k
				0.1,10.5,0.1 //Phi default 1
				);
			return 0;
		case 6:
			szenarios::swipe_equilibrium(
				0.1,0.8,0.001, //k
				10.,10.4,0.5 //Phi default 1
				);
			return 0;
		default:
			cout << "Please select valid option!" << endl;
			goto start;
	};
	return 0;
}


