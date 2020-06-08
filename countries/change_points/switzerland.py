""" # Switzerland
    

These were chosen by using the [Wikipedia timeline](https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Poland#Timeline)

"""
import datetime

"""
We choose the following change points:
* __28/02__ Cancle mass events
Federal Council banned events involving more than 1,000 people in an effort to curb the spread of the infection
"""
_28_02 = dict(
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
* __13/03__ Schools closed
 Federal Council decided to cancel classes in all educational establishments until 4 April 2020,
 and has banned all events (public or private) involving more than 100 people

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
* __16/03__ Further restrictions
Federal Council announced further measures, and a revised ordinance. Measures include the closure of bars,
shops and other gathering places until 19 April,
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
* __20/03__ Public mettings are prohibited
The government announced that no lockdown would be implemented, but all events or meetings over 5 people were prohibited.
"""
_20_03 = dict(
    pr_median_lambda=0.1,
    pr_sigma_lambda=0.3,  # gives pymc3 a hard time
    pr_sigma_date_transient=2,
    pr_median_transient_len=4,
    pr_sigma_transient_len=0.5,
    pr_mean_date_transient=datetime.datetime(2020,3,20),
    relative_to_previous=False,
    pr_factor_to_previous=1,
)


"""
Now we put all changepoints together into an array. The name of this variable has to be the same for
every country file! Otherwise the change points getter in change_points.py will not work
"""
cps=[_13_03,_16_03,_20_03]