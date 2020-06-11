""" # Measures for Italy

We look at the different measures as can be seen on
"""

""" ## Imports
"""
import datetime
import sys

# Go into main folder and import our python files which include the class
sys.path.append("../")
import keywords as kw
from measure import Measure  # Our Measure helper class


""" ## Measures
Sources are
[Ferguson et al. March 2020](https://www.imperial.ac.uk/mrc-global-infectious-disease-analysis/covid-19/report-13-europe-npi-impact/)
"""
measures = []  # Create empty array on which we append later on

"""
March 5:
"""
begin = datetime.datetime(2020, 3, 5)
keyword = dict(
    tag=kw.close_schools,
    description=""" Nationwide school closures."""
    )
measures.append(Measure(keyword, begin))


"""
March 9:
"""
begin = datetime.datetime(2020, 3, 9)
keyword = dict(
    tag=kw.stay_home_if_cough,
    description=""" Advice to self-isolate if experiencing symptoms."""
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 9)
keyword = dict(
    tag=kw.case_based_isolation,
    description=""" quarantine if tested positive """
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 9)
keyword = dict(
    tag=kw.forbid_assemblies_all,
    description=""" The government bans all public events."""
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 9)
keyword = dict(
    tag=kw.keep_distance,
    description=""" A distance of more than 1m has to be kept and any other form
                    of alternative aggregation is to be excluded."""
    )
measures.append(Measure(keyword, begin))


"""
March 11:
"""
begin = datetime.datetime(2020, 3, 11)
keyword = dict(
    tag=kw.lockdown,
    description=""" The government closes all public places. People have to stay
                    at home except for essential travel."""
    )
measures.append(Measure(keyword, begin))
