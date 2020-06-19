""" # Measures for Norway

TODO: Add reopening
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
    tag=kw.forbid_assemblies_all,
    description=""" The Directorate of Health bans all non-necessary social contact."""
    )
measures.append(Measure(keyword, begin))


"""
March 13:
"""
begin = datetime.datetime(2020, 3, 13)
keyword = dict(
    tag=kw.close_schools,
    description=""" Norwegian Directorate of Health closes all educational
                    institutions. Including childcare facilities and all schools."""
    )
measures.append(Measure(keyword, begin))


"""
March 15:
"""
begin = datetime.datetime(2020, 3, 15)
keyword = dict(
    tag=kw.stay_home_if_cough,
    description=""" Advice to self-isolate for 7 days if experiencing a cough or
                    fever symptoms"""
    )
measures.append(Measure(keyword, begin))


"""
March 16:
"""
begin = datetime.datetime(2020, 3, 16)
keyword = dict(
    tag="social distancing",
    description=""" The Directorate of Health advises against all travelling and
                    non-necessary social contacts. """
    )
measures.append(Measure(keyword, begin))


"""
March 24:
"""
begin = datetime.datetime(2020, 3, 24)
keyword = dict(
    tag=kw.lockdown,
    description=""" Only people living together are allowed outside together."""
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 24)
keyword = dict(
    tag=kw.keep_distance,
    description=""" Everyone has to keep a 2m distance."""
    )
measures.append(Measure(keyword, begin))
