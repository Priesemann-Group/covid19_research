""" # Belgium
    
https://www.euractiv.com/section/coronavirus/news/belgium-enters-lockdown-over-coronavirus-crisis-until-5-april/

These were chosen by using the [Wikipedia timeline](https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Belgium#Timeline)
and the [Imperial College Report](https://www.imperial.ac.uk/media/imperial-college/medicine/mrc-gida/2020-03-30-COVID19-Report-13.pdf).

"""
import datetime

"""
We choose the following change points:
* __13/03__ Ban on public event
* __14/03__ Schools closed
    The school closure was offically on 14th but we predict the change point for the
    pulblic events to be the same one as the school closing.
    https://www.info-coronavirus.be/en/news/phase-2-maintained-transition-to-the-federal-phase-and-additional-measures/
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
* __18/03__ Lockdown ordered
    https://www.belgium.be/en/news/2020/coronavirus_reinforced_measures
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
* __05/04__ Lockdown relaxed and mandatory masks in public transport
"""
_05_04 = dict(
    pr_median_lambda=0.1,
    pr_sigma_lambda=0.3,  # gives pymc3 a hard time
    pr_sigma_date_transient=2,
    pr_median_transient_len=4,
    pr_sigma_transient_len=0.5,
    pr_mean_date_transient=datetime.datetime(2020,4,5),
    relative_to_previous=False,
    pr_factor_to_previous=1,
)

"""
Now we put all changepoints together into an array. The name of this variable has to be the same for
every country file! Otherwise the change points getter in change_points.py will not work
"""

cps=[_13_03,_18_03,_05_04]