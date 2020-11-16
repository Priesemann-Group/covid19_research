#include "utils.h"


//======================================================================
// Returns interpolated value at x from parallel arrays ( xData, yData )
// Assumes that xData has at least two elements, is sorted and is strictly monotonic increasing
// boolean argument extrapolate determines behaviour beyond ends of array (if needed)
double interpolate( vector<double> &xData, vector<double> &yData, double x, bool extrapolate )
{
   int size = xData.size();

   int i = 0;                                                                  // find left end of interval for interpolation
   if ( x >= xData[size - 2] )                                                 // special case: beyond right end
   {
      i = size - 2;
   }
   else
   {
      while ( x > xData[i+1] ) i++;
   }
   double xL = xData[i], yL = yData[i], xR = xData[i+1], yR = yData[i+1];      // points on either side (unless beyond ends)
   if ( !extrapolate )                                                         // if beyond ends of array and not extrapolating
   {
      if ( x < xL ) yR = yL;
      if ( x > xR ) yL = yR;
   }

   double dydx = ( yR - yL ) / ( xR - xL );                                    // gradient

   return yL + dydx * ( x - xL );                                              // linear interpolation
}



//Function for time modulation
double logistics(double t,
   double center, double length, double change) {
   /*
   Parameterized logistics function see model based and free paper
   */
   return change/(1 + exp(-4.0/length * (t-center)));
};


double gaussian_peak(double t,
   double mean, double variance, double change) {
   /*
   Parameterized peak function to have a height called change
   */
   return change * exp(-(t-mean)*(t-mean)/(2*variance*variance));
}

vector<double> convolve(const vector<double>& a, const vector<double>& b)
{
    int n_a = a.size();
    int n_b = b.size();
    vector<double> result(n_a + n_b - 1);

    for (int i = 0; i < n_a + n_b - 1; ++i) {
        double sum = 0.0;
        for (int j = 0; j <= i; ++j) {
            sum += ((j < n_a) && (i-j < n_b)) ? a[j]*b[i-j] : 0.0;
        }
        result[i] = sum;
    }
    return result;
}
double gamma_pdf(double x,double a, double b){
   return pow(x,a-1.0)*exp(-x)/tgamma(a);
}


std::vector<double> get_new_cases(data_struct &data, Model &model){
   std::vector<double> N;
   double gamma = model.gamma;


   for (unsigned long int i = 0; i < data.time.size(); ++i)
   {
      N.push_back(
         gamma * model.k(data.time[i]) * model.R_0 * data.system[i][0]/model.M * data.system[i][4] +
         gamma * (model.nu+model.epsilon)*model.R_0*
         data.system[i][0]/model.M * data.system[i][3]
         +model.Phi(data.time[i])*data.system[i][0]/model.M
      );
   }
   return N;
};

vector<double> get_new_cases_obs(data_struct &data, Model &model){

   vector<double> N_obs;

   //Model params
   double N_test,N_traced;
   double chi_sr = model.chi_sr();
   double chi_r = model.chi_r();
   double xi = model.xi;
   double rho = model.rho;

   //Calc vector
   vector<double> part_1;
   for (long unsigned int i = 0; i < data.time.size(); ++i)
   {
      N_test = model.N_test(data.system[i][4],data.system[i][5]);
      N_traced = model.N_traced(data.time[i]);
      part_1.push_back(rho*data.system[i][1]+N_test+(chi_sr*(1.0-xi)+chi_r*xi)*N_traced);
   }

   // For gamma kernel we need approx 11days
   vector<double> part_2;
   int count = 0;
   for (long unsigned int i = 0; i < data.time.size(); ++i)
   {
      if (data.time[i] > 12.0) break;
      part_2.push_back(gamma_pdf(data.time[i],4.0,1.0));
      count ++;
   }

   //Normalize kernel
   double sum = 0.0;
   for (long unsigned int i = 0; i < part_2.size(); ++i)
   {
      sum += part_2[i];
   }
   for (long unsigned int i = 0; i < part_2.size(); ++i)
   {
      part_2[i] = part_2[i]/sum;
      //cout << part_2[i] << endl;
   }

   //Do convolution
   N_obs = convolve(part_1,part_2);
   //We remove from the front the half size of conv. from the vector
   N_obs.erase(N_obs.end()-count,N_obs.end());

   return N_obs;
};


void save_to_file(data_struct &data, Model &model,string fpath){
   //Save data
   ofstream myfile;
   myfile.open(fpath);

   //Get new cases;
   vector<double> N_obs = get_new_cases_obs(data,model); 
   vector<double> N = get_new_cases(data,model); 
   //Header
   myfile << 
"time,\
Susceptible,\
Exposed (quarantined),\
Exposed (hidden),\
Infectious (quarantined),\
Infectious (hidden),\
Infectious (hidden susceptible),\
Recovered,\
Reprodcution (hidden),\
Influx,\
Contact,\
N_traced,\
New cases,\
New cases observed"
   << std::endl;


   for (long unsigned int i = 0; i < data.time.size(); ++i)
   {
      myfile << data.time[i] << ", ";
      for (long unsigned int j = 0; j < data.system[0].size();j++){
         myfile << data.system[i][j] << ", ";
      }
      myfile << model.k(data.time[i])*model.R_0 << ", ";
      myfile << model.Phi(data.time[i]) << ", ";
      myfile << model.k(data.time[i]) << ", ";
      myfile << model.N_traced(data.time[i]) << ", ";
      myfile << N[i] << ", ";
      myfile << N_obs[i];
      myfile << std::endl;
   }
   myfile.close();
   //cout << "Saved to file" << std::endl;
}

string convert_double_to_fixed(double in, int precision){
   std::stringstream stream;
   stream << std::fixed << std::setprecision(precision) << in;
   std::string s = stream.str();
   return s;
}

