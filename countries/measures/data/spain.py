""" # Measures for Spain
Look into these official sources for reopening:
* https://www.boe.es/eli/es/o/2020/05/16/snd414/con
* https://www.boe.es/eli/es/o/2020/05/30/snd458
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
March 9:
"""
begin = datetime.datetime(2020, 3, 9)
keyword = dict(
    tag=kw.work_from_home,
    description=""" working remotely from home"""
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 9)
keyword = dict(
    tag="social distancing",
    description=""" Advice on social distancing"""
    )
measures.append(Measure(keyword, begin))


"""
March 13:
"""
begin = datetime.datetime(2020, 3, 13)
keyword = dict(
    tag=kw.close_schools,
    description=""" Nationwide school closures."""
    )
measures.append(Measure(keyword, begin))


"""
March 14:
"""
begin = datetime.datetime(2020, 3, 14)
keyword = dict(
    tag=kw.lockdown,
    description=""" Nationwide lockdown."""
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 14)
keyword = dict(
    tag=kw.forbid_assemblies_all,
    description=""" Banning of all public events by lockdown."""
    )
measures.append(Measure(keyword, begin))


"""
March 17:
"""
begin = datetime.datetime(2020, 3, 17)
keyword = dict(
    tag=kw.stay_home_if_cough,
    description=""" Advice to self-isolate for 7 days if experiencing a cough or
                    fever symptoms."""
    )
measures.append(Measure(keyword, begin))
