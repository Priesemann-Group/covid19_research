""" # Measures for Switzerland

One has to look at this once more
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
[wikipedia](https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Switzerland)
[Ferguson et al. March 2020](https://www.imperial.ac.uk/mrc-global-infectious-disease-analysis/covid-19/report-13-europe-npi-impact/)
"""

"""
February 28:
"""
begin = datetime.datetime(2020, 2, 28)
keyword = dict(
    tag=kw.forbid_assemblies_1000,
    description=""" The Federal Council banned events involving more than
                    1,000 people in an effort to curb the spread of the infection. """
)
measures.append(Measure(keyword, begin))


"""
March 2:
"""
begin = datetime.datetime(2020, 3, 2)
keyword = dict(
    tag=kw.stay_home_if_cough,
    description=""" Advice to self-isolate if experiencing a cough or fever symptoms. """
)
measures.append(Measure(keyword, begin))


"""
March 14:
"""
begin = datetime.datetime(2020, 3, 14)
keyword = dict(
    tag=kw.close_schools,
    description=""" The Federal Council decided to cancel classes in all educational
                    establishments. """
)
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,5,11)))
keyword = dict(
    tag=kw.close_universities,
    description=""" The Federal Council decided to cancel classes in all educational
                    establishments. """
)
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,6,8)))
keyword = dict(
    tag="forbid assemblies > 100 people",
    description=""" The Federal Council has banned all events (public or private) involving
                    more than 100 people. """
)
measures.append(Measure(keyword, begin))
keyword = dict(
    tag="border closed",
    description=""" The Federal Council has also decided to partially close
                    its borders and enacted border controls. """
)
measures.append(Measure(keyword, begin))

"""
March 16:
"""
begin = datetime.datetime(2020, 3, 16)
keyword = dict(
    tag=kw.close_shops,
    description=""" The Federal Council announced further measures, include the
                    closure of bars, shops and other gathering places. """
)
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,5,11)))
keyword = dict(
    tag=kw.close_res_bars,
    description=""" The Federal Council announced further measures, include the
                    closure of bars, shops and other gathering places. """
)
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,5,11)))

"""
March 20:
"""
begin = datetime.datetime(2020, 3, 20)
keyword = dict(
    tag=kw.forbid_assemblies_all,
    description=""" The government announced that no lockdown would be implemented,
                    but all events or meetings over 5 people were prohibited. """
)
measures.append(Measure(keyword, begin))
