""" # Austria
    
The change points are mostly copied from
https://github.com/Konrad982/covid19_inference/blob/master/scripts/Austria_JHU.ipynb.

These were chosen by using the [Wikipedia timeline](https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Austria)
and the [Imperial College Report](https://www.imperial.ac.uk/media/imperial-college/medicine/mrc-gida/2020-03-30-COVID19-Report-13.pdf).

"""
import datetime

"""
We choose the following change points:
* __10/03__ Ban on public events
    All outdoor events with more than 500 people and all indoor events with more than 100 people were cancelled.
"""
_10_03 = dict(
    pr_median_lambda=0.1,
    pr_sigma_lambda=0.3,  # gives pymc3 a hard time
    pr_sigma_date_transient=2,
    pr_median_transient_len=4,
    pr_sigma_transient_len=0.5,
    pr_mean_date_transient=datetime.datetime(2020,3,10),
    relative_to_previous=False,
    pr_factor_to_previous=1,
)

"""
* __16/03__ Schools closed
    We assume school closures to take effect on Monday together with the strong social distancing
    [ref](https://www.kleinezeitung.at/politik/5783037/Coronavirus_Stufenweise-ab-Montag_Oesterreich-schliesst-Schulen)
"""
_16_03 = dict(
    pr_median_lambda=0.1,
    pr_sigma_lambda=0.3,  # gives pymc3 a hard time
    pr_sigma_date_transient=2,
    pr_median_transient_len=4,
    pr_sigma_transient_len=0.5,
    pr_mean_date_transient=datetime.datetime(2020,3,16),
    relative_to_previous=False,
    pr_factor_to_previous=1,
)

"""
* __30/03__ Mask obligations in stores
"""
_30_03 = dict(
    pr_median_lambda=0.1,
    pr_sigma_lambda=0.3,  # gives pymc3 a hard time
    pr_sigma_date_transient=2,
    pr_median_transient_len=4,
    pr_sigma_transient_len=0.5,
    pr_mean_date_transient=datetime.datetime(2020,3,30),
    relative_to_previous=False,
    pr_factor_to_previous=1,
)

"""
* __30/04__ Rules relaxed but also further mask obligation
"""
_30_04 = dict(
    pr_median_lambda=0.1,
    pr_sigma_lambda=0.3,  # gives pymc3 a hard time
    pr_sigma_date_transient=2,
    pr_median_transient_len=4,
    pr_sigma_transient_len=0.5,
    pr_mean_date_transient=datetime.datetime(2020,4,30),
    relative_to_previous=False,
    pr_factor_to_previous=1,
)

"""
Now we put all changepoints together into an array. The name of this variable has to be the same for
every country file! Otherwise the change points getter in change_points.py will not work
"""

cps=[_10_03,_16_03,_30_03,_30_04]