""" # Measures for Italy
Measures like close theaters still missing.
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
[Official comrpehensive list by the government (in Italian)](http://www.governo.it/it/coronavirus-misure-del-governo)
"""
measures = []  # Create empty array on which we append later on

"""
January 30:
"""
begin = datetime.datetime(2020, 1, 30)
keyword = dict(
    tag="cancel flights China",
    description=""" The Prime Minister declared that, on the orders of the national
                    health authorities,  all flights to and from China are suspended - in addition
                    to those from Wuhan, already suspended by the Chinese authorities.""",  # actually, on February 1 cargo flights were reenabled.
)
measures.append(Measure(keyword, begin))

# There are some other measures concercing e.g. thermoscanners in airports, controls for ships, ...

"""
February 21:
"""
begin = datetime.datetime(2020, 2, 21)
keyword = dict(
    tag=kw.case_based_isolation,
    description=""" People returning from risk areas have to signal themselves and are asked to stay in quarantine for 14 days. People having had contact with an infected person have to follow an obligatory 14-day quarantine.""",
)
measures.append(Measure(keyword, begin))

# several local / regional measures in Northern Italy on February 23, 25, see
# https://www.gazzettaufficiale.it/eli/id/2020/02/25/20A01278/sg
# and
# https://www.gazzettaufficiale.it/eli/id/2020/02/23/20A01228/sg
# for Italian law texts

# other regional measures possible

# school and university closures occurred much earlier in popolous regions in the north (Lombardia, Veneto, Emilia-Romagna, maybe also Liguria, Piemonte, Trentino-Alto Adige/Südtirol). This should be taken into account for modelling as the virus spread there (first in Veneto and Lombardy)

"""
March 5:
"""
begin = datetime.datetime(2020, 3, 5)
keyword = dict(tag=kw.close_schools, description=""" Nationwide school closures.""")
measures.append(Measure(keyword, begin))
keyword = dict(
    tag=kw.close_universities, description=""" Nationwide university closures."""
)
measures.append(Measure(keyword, begin))

# 8 march: no more travel from Lombardy and 14 provinces in other regions to other parts of Italy
# the measures of march 10 came into effect earlier in some regions in the north
"""
March 10:
"""
begin = datetime.datetime(2020, 3, 10)
keyword = dict(
    tag=kw.stay_home_if_cough,
    description=""" Advice to self-isolate if experiencing symptoms.""",
)  # this was probably earlier
measures.append(Measure(keyword, begin))

keyword = dict(
    tag=kw.forbid_assemblies_all,
    description=""" The government bans all public events.""",
)
measures.append(Measure(keyword, begin))

keyword = dict(
    tag=kw.keep_distance,
    description=""" A distance of more than 1m has to be kept and any other form
                    of alternative aggregation is to be excluded.""",
)
measures.append(Measure(keyword, begin))


"""
March 10:
"""
begin = datetime.datetime(2020, 3, 10)
keyword = dict(
    tag=kw.lockdown,
    description=""" The government closes all public places. People have to stay
                    at home except for essential travel.""",
)
measures.append(
    Measure(keyword, begin, end=datetime.datetime(2020, 5, 4))
)  # the lockdown mainly ended on May 4

keyword = dict(
    tag=kw.close_shops,
    description=""" In a video, the President announced  the closure of all commercial
                    and retail activities, with the exception of grocery stores,
                    basic necessities, pharmacies and parapharmacies.""",
)
measures.append(Measure(keyword, begin, end=datetime.datetime(2020, 5, 18)))


"""
March 21:
"""
begin = datetime.datetime(2020, 3, 21)
keyword = dict(
    tag="close public places",
    description=""" The  Minister of Health signed the ordinance prohibiting: public
                    access to parks, villas, play areas and public gardens; to play
                    games or outdoor recreation. It is permitted to carry out individual
                    physical activities in the vicinity of one's home, provided that,
                    in any case, respecting the distance of at least one meter from
                    each other person.""",
)
measures.append(Measure(keyword, begin, end=datetime.datetime(2020, 5, 4)))


"""
March 23:
"""
begin = datetime.datetime(2020, 3, 23)
keyword = dict(
    tag="no travel",
    description=""" A new ordinance has been adopted jointly by the Minister of
                    Health and the Minister of the Interior which prohibits all
                    natural persons from moving or moving with public or private
                    means of transport in a municipality other than that in which
                    they are located, except for proven work needs, of absolute
                    urgency or for health reasons.""",
)
measures.append(
    Measure(keyword, begin, end=datetime.datetime(2020, 5, 18))
)  # gradually from May 4
