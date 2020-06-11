""" # Measures for Belgium

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
March 12:
"""
begin = datetime.datetime(2020, 3, 12)
keyword = dict(
    tag="forbid assemblies > 500",
    description=""" The government bans events >500 people."""
    )
measures.append(Measure(keyword, begin))


"""
March 16:
"""
begin = datetime.datetime(2020, 3, 16)
keyword = dict(
    tag=kw.work_from_home,
    description=""" encouragement to work from home."""
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 16)
keyword = dict(
    tag=kw.stay_home_if_cough,
    description=""" People even with mild symptoms are told to limit social contact."""
    )
measures.append(Measure(keyword, begin))


"""
March 18:
"""
begin = datetime.datetime(2020, 3, 18)
keyword = dict(
    tag=kw.close_schools,
    description=""" Colleges and upper secondary schools shut."""
    )
measures.append(Measure(keyword, begin))
