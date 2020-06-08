""" # Poland
    

These were chosen by using the [Wikipedia timeline](https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Poland#Timeline)

"""
import datetime

"""
We choose the following change points:
* __10/03__ Cancle mass events
On 10 March, authorities cancelled all mass events, defined as those allowing 1000 or more participants
in the case of stadiums or other events outside of buildings, and those allowing 500 or more participants
in the case of events in buildings.
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
* __12/03__ Schools closed
"""
_12_03 = dict(
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
* __24/03__ Further restrictions

Poland's government announced further restrictions on people leaving their homes and on public gatherings
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
* __10/04__ Schools opened again
"""
_10_04 = dict(
    pr_median_lambda=0.1,
    pr_sigma_lambda=0.3,  # gives pymc3 a hard time
    pr_sigma_date_transient=2,
    pr_median_transient_len=4,
    pr_sigma_transient_len=0.5,
    pr_mean_date_transient=datetime.datetime(2020,4,10),
    relative_to_previous=False,
    pr_factor_to_previous=1,
)


"""
Now we put all changepoints together into an array. The name of this variable has to be the same for
every country file! Otherwise the change points getter in change_points.py will not work
"""
cps=[_10_03,_12_03,_24_03,_10_04]