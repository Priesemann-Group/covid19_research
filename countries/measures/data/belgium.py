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
March 10:
"""
begin = datetime.datetime(2020, 3, 10)
keyword = dict(
    tag=kw.stay_home_if_cough,
    description=""" Everyone should stay at home if experiencing a cough or fever."""
    )
measures.append(Measure(keyword, begin))


"""
March 12:
"""
begin = datetime.datetime(2020, 3, 12)
keyword = dict(
    tag=kw.forbid_assemblies_all,
    description=""" All recreational activities cancelled regardless of size."""
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

begin = datetime.datetime(2020, 3, 14)
keyword = dict(
    tag=kw.avoid_public_transport,
    description=""" Public transport recommended only for essential journeys """
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 14)
keyword = dict(
    tag=kw.work_from_home,
    description=""" work from home encouraged """
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 14)
keyword = dict(
    tag=kw.close_res_bars,
    description=""" all public places e.g. restaurants closed """
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 14)
keyword = dict(
    tag=kw.close_shops,
    description=""" all public places e.g. restaurants closed """
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 14)
keyword = dict(
    tag=kw.close_theaters_cinema,
    description=""" all public places e.g. restaurants closed """
    )
measures.append(Measure(keyword, begin))


"""
March 18:
"""
begin = datetime.datetime(2020, 3, 18)
keyword = dict(
    tag=kw.lockdown,
    description=""" Citizens are required to stay at home except for work and
                    essential journeys. Going outdoors only with household
                    members or 1 friend."""
    )
measures.append(Measure(keyword, begin))



begin = datetime.datetime(2020, 3, 16)
keyword = dict(
    tag=kw.case_based_isolation,
    description=""" Implemented at lockdown."""
    )
measures.append(Measure(keyword, begin))
