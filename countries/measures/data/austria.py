""" # Measures for Austria

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
March 10:
"""
begin = datetime.datetime(2020, 3, 10)
keyword = dict(
    tag=kw.forbid_assemblies_all,
    description=""" Banning of gatherings of more than 5 people."""
    )
measures.append(Measure(keyword, begin))

"""
March 14:
"""
begin = datetime.datetime(2020, 3, 14)
keyword = dict(
    tag=kw.close_schools,
    description=""" Nationwide school closures."""
    )
measures.append(Measure(keyword, begin))

"""
March 16:
"""
begin = datetime.datetime(2020, 3, 16)
keyword = dict(
    tag=kw.lockdown,
    description=""" Banning all access to public spaces and gatherings of more
                    than 5 people."""
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 16)
keyword = dict(
    tag=kw.keep_distance,
    description=""" Recommendation to maintain a distance of 1m."""
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 16)
keyword = dict(
    tag=kw.case_based_isolation,
    description=""" Implemented at lockdown."""
    )
measures.append(Measure(keyword, begin))
