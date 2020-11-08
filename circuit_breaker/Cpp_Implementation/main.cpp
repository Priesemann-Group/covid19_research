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
  int x;
	cin >> x;

	switch(x){
		case 1:
			szenarios::parameter_swipe_ld_dates();
			return 0;
		case 2:
			szenarios::stable_model_to_tipping_point();
			return 0;
		default:
			cout << "Please select valid option!" << endl;
			goto start;
	};
	return 0;
}


