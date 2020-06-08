""" # Netherlands
    
The change points are mostly copied from
https://github.com/Konrad982/covid19_inference/blob/master/scripts/Netherlands_JHU.ipynb.

These were chosen by using the [Wikipedia timeline](https://en.wikipedia.org/wiki/COVID-19_pandemic_in_the_Netherlands)
and the [Imperial College Report](https://www.imperial.ac.uk/media/imperial-college/medicine/mrc-gida/2020-03-30-COVID19-Report-13.pdf).

"""
import datetime

"""
We choose the following change points:
* __11/03__ Stricter measures in North Brabant
* __10/03__ Closure of schools
* __12/03__ Ban on public events 
"""
_11_03 = dict(
    pr_median_lambda=0.1,
    pr_sigma_lambda=0.3,  # gives pymc3 a hard time
    pr_sigma_date_transient=2,
    pr_median_transient_len=4,
    pr_sigma_transient_len=0.5,
    pr_mean_date_transient=datetime.datetime(2020,3,11),
    relative_to_previous=False,
    pr_factor_to_previous=1,
)

"""
* __15/03__ Stricter measures
"""
_15_03 = dict(
    pr_median_lambda=0.1,
    pr_sigma_lambda=0.3,  # gives pymc3 a hard time
    pr_sigma_date_transient=2,
    pr_median_transient_len=4,
    pr_sigma_transient_len=0.5,
    pr_mean_date_transient=datetime.datetime(2020,3,15),
    relative_to_previous=False,
    pr_factor_to_previous=1,
)

"""
* __23/03__ Strict social distancing
"""
_23_03 = dict(
    pr_median_lambda=0.1,
    pr_sigma_lambda=0.3,  # gives pymc3 a hard time
    pr_sigma_date_transient=2,
    pr_median_transient_len=4,
    pr_sigma_transient_len=0.5,
    pr_mean_date_transient=datetime.datetime(2020,3,23),
    relative_to_previous=False,
    pr_factor_to_previous=1,
)

"""
Now we put all changepoints together into an array. The name of this variable has to be the same for
every country file! Otherwise the change points getter in change_points.py will not work
"""

cps=[_11_03,_15_03,_23_03]