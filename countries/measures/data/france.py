""" # Measures for France

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
March 13:
"""
begin = datetime.datetime(2020, 3, 13)
keyword = dict(
    tag="forbid assemblies > 100",
    description=""" Bans of events >100 people."""
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
March 17:
"""
begin = datetime.datetime(2020, 3, 17)
keyword = dict(
    tag=kw.lockdown,
    description=""" Everybody has to stay at home. Need a selfauthorisation
                    form to leave home. """
    )
measures.append(Measure(keyword, begin))
