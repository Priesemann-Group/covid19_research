""" # Measures for Denmark

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
    tag="ban assemblies > 100",
    description=""" Bans of events >100 people."""
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 12)
keyword = dict(
    tag=kw.close_theaters_cinema,
    description=""" closed cultural institutions, leisure facilities etc """
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 12)
keyword = dict(
    tag=kw.stay_home_if_cough,
    description=""" Everyone should stay at home if experiencing a cough or fever."""
    )
measures.append(Measure(keyword, begin))


"""
March 13:
"""
begin = datetime.datetime(2020, 3, 13)
keyword = dict(
    tag="close secondary schools",
    description=""" Secondary schools shut and universities
                    (primary schools also shut on 16th)."""
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 13)
keyword = dict(
    tag=kw.avoid_public_transport,
    description=""" Limited use of public transport """
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 13)
keyword = dict(
    tag=kw.keep_distance,
    description=""" recommend keeping appropriate distance """
    )
measures.append(Measure(keyword, begin))


"""
March 16:
"""
begin = datetime.datetime(2020, 3, 16)
keyword = dict(
    tag="close primary schools",
    description=""" Secondary schools shut and universities
                    (primary schools also shut on 16th)."""
    )
measures.append(Measure(keyword, begin))


"""
March 18:
"""
begin = datetime.datetime(2020, 3, 18)
keyword = dict(
    tag=kw.lockdown,
    description=""" Bans of gatherings of >10 people in public and all public
                    places were shut."""
    )
measures.append(Measure(keyword, begin))
