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
[Wikipedia](https://en.wikipedia.org/wiki/COVID-19_pandemic_in_France#Lockdown)
Personal following of press
"""
measures = []  # Create empty array on which we append later on


"""
March 10:
"""
begin = datetime.datetime(2020, 3, 10)  # according to Wikipedia
keyword = dict(
    tag="forbid assemblies > 1000", description=""" Bans of events >1000 people."""
)
measures.append(Measure(keyword, begin))

"""
March 14:
"""
begin = datetime.datetime(2020, 3, 14)  # according to Wikipedia
keyword = dict(
    tag="forbid assemblies > 100", description=""" Bans of events >100 people."""
)
measures.append(Measure(keyword, begin))

"""
March 16:
"""
begin = datetime.datetime(2020, 3, 16)
keyword = dict(
    tag=kw.close_schools,
    description=""" Nationwide school closures became effective, including universities.""",  # announced on saturday, 14/03, falls essentially together with closure of non-essential services, effective one day earlier
)
measures.append(Measure(keyword, begin))


"""
March 17:
"""
begin = datetime.datetime(2020, 3, 17)
keyword = dict(
    tag=kw.lockdown,
    description=""" Everybody has to stay at home. Need a selfauthorisation
                    form to leave home. """,
)
measures.append(Measure(keyword, begin))
