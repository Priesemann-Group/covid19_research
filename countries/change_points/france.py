""" # France
    
These were chosen by using the [Wikipedia timeline](https://en.wikipedia.org/wiki/COVID-19_pandemic_in_France)
and the [Imperial College Report](https://www.imperial.ac.uk/media/imperial-college/medicine/mrc-gida/2020-03-30-COVID19-Report-13.pdf).

"""
import datetime

"""
We choose the following change points:
* __14/03__ Ban on gatherings
    Bans on gatherings over 100ppl
"""
_14_03 = dict(
    pr_median_lambda=0.1,
    pr_sigma_lambda=0.3,  # gives pymc3 a hard time
    pr_sigma_date_transient=2,
    pr_median_transient_len=4,
    pr_sigma_transient_len=0.5,
    pr_mean_date_transient=datetime.datetime(2020,3,12),
    relative_to_previous=False,
    pr_factor_to_previous=1,
)

"""
* __17/03__ Nationwide lockdown
"""
_17_03 = dict(
    pr_median_lambda=0.1,
    pr_sigma_lambda=0.3,  # gives pymc3 a hard time
    pr_sigma_date_transient=2,
    pr_median_transient_len=4,
    pr_sigma_transient_len=0.5,
    pr_mean_date_transient=datetime.datetime(2020,3,17),
    relative_to_previous=False,
    pr_factor_to_previous=1,
)

"""
* __24/03__ Lockdown measures strengthened (a bit)
"""
_24_03 = dict(
    pr_median_lambda=0.1,
    pr_sigma_lambda=0.3,  # gives pymc3 a hard time
    pr_sigma_date_transient=2,
    pr_median_transient_len=4,
    pr_sigma_transient_len=0.5,
    pr_mean_date_transient=datetime.datetime(2020,3,24),
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
* __11_05__ Lockdown lifting phase 1
"""
_11_05 = dict(
    pr_median_lambda=0.1,
    pr_sigma_lambda=0.3,  # gives pymc3 a hard time
    pr_sigma_date_transient=2,
    pr_median_transient_len=4,
    pr_sigma_transient_len=0.5,
    pr_mean_date_transient=datetime.datetime(2020,5,11),
    relative_to_previous=False,
    pr_factor_to_previous=1,
)

"""
Now we put all changepoints together into an array. The name of this variable has to be the same for
every country file! Otherwise the change points getter in change_points.py will not work
"""

cps=[_14_03,_17_03,_24_03,_30_04,_11_05]