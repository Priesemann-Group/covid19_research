""" # Denmark
    
These were chosen by using the [Wikipedia timeline](https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Denmark#Timeline)

"""
import datetime

"""
We choose the following change points:
* __11/03__ Big events canceled
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
* __13/03__ Lockdown public sector
"""
_13_03 = dict(
    pr_median_lambda=0.1,
    pr_sigma_lambda=0.3,  # gives pymc3 a hard time
    pr_sigma_date_transient=2,
    pr_median_transient_len=4,
    pr_sigma_transient_len=0.5,
    pr_mean_date_transient=datetime.datetime(2020,3,13),
    relative_to_previous=False,
    pr_factor_to_previous=1,
)

"""
* __16/03__ Schools closed
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
* __18/03__ Contact ban
"""
_18_03 = dict(
    pr_median_lambda=0.1,
    pr_sigma_lambda=0.3,  # gives pymc3 a hard time
    pr_sigma_date_transient=2,
    pr_median_transient_len=4,
    pr_sigma_transient_len=0.5,
    pr_mean_date_transient=datetime.datetime(2020,3,18),
    relative_to_previous=False,
    pr_factor_to_previous=1,
)

"""
* __15/04 Reopening of schools
    https://www.altinget.dk/artikel/mette-frederiksen-de-mindste-boern-kan-begynde-i-skole-og-daginstitutioner-naeste-uge
"""
_15_04 = dict(
    pr_median_lambda=0.1,
    pr_sigma_lambda=0.3,  # gives pymc3 a hard time
    pr_sigma_date_transient=2,
    pr_median_transient_len=4,
    pr_sigma_transient_len=0.5,
    pr_mean_date_transient=datetime.datetime(2020,4,15),
    relative_to_previous=False,
    pr_factor_to_previous=1,
)

"""
Now we put all changepoints together into an array. The name of this variable has to be the same for
every country file! Otherwise the change points getter in change_points.py will not work
"""

cps=[_11_03,_13_03,_16_03,_18_03,_15_04]