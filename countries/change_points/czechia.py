""" # Czechia
    
Alot of things were copied from https://github.com/Konrad982/covid19_inference/blob/master/scripts/Czech_Republic_JHU.ipynb

TODO:
This needs some more work, since the table on the wikipedia page gives alot of more infos (as of now).

These were chosen by using the [Wikipedia timeline](https://en.wikipedia.org/wiki/COVID-19_pandemic_in_the_Czech_Republic#Policies_to_fight_the_contagion)

"""
import datetime

"""
We choose the following change points:
* __07/03__ Quarantine
"""
_07_03 = dict(
    pr_median_lambda=0.1,
    pr_sigma_lambda=0.3,  # gives pymc3 a hard time
    pr_sigma_date_transient=2,
    pr_median_transient_len=4,
    pr_sigma_transient_len=0.5,
    pr_mean_date_transient=datetime.datetime(2020,3,7),
    relative_to_previous=False,
    pr_factor_to_previous=1,
)

"""
* __13/03__ Closures
    https://www.belgium.be/en/news/2020/coronavirus_reinforced_measures
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
* __16/03__ Curfew
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
* __24/04__ Curfew loosened
"""
_24_04 = dict(
    pr_median_lambda=0.1,
    pr_sigma_lambda=0.3,  # gives pymc3 a hard time
    pr_sigma_date_transient=2,
    pr_median_transient_len=4,
    pr_sigma_transient_len=0.5,
    pr_mean_date_transient=datetime.datetime(2020,4,24),
    relative_to_previous=False,
    pr_factor_to_previous=1,
)


"""
Now we put all changepoints together into an array. The name of this variable has to be the same for
every country file! Otherwise the change points getter in change_points.py will not work
"""

cps=[_07_03,_13_03,_16_03,_24_04]