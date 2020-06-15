""" # Measures for Estonia
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
[Wikipedia](https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Estonia)
"""
measures = []  # Create empty array on which we append later on

"""
March 13:

https://news.err.ee/1063224/estonian-government-declares-emergency-situation-against-coronavirus
"""
begin = datetime.datetime(2020, 3, 13)
keyword = dict(
    tag=kw.forbid_assemblies_all,
    description=""" The Estonian government declared a state of emergency until 1 May.
                    All public gatherings were banned, including sports and cultural events;
                    schools and universities were closed; border control was restored with
                    health checks at every crossing and entry point """
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020,5,1)))

keyword = dict(
    tag=kw.cancel_football,
    description=""" The Estonian government declared a state of emergency until 1 May.
                    All public gatherings were banned, including sports and cultural events;
                    schools and universities were closed; border control was restored with
                    health checks at every crossing and entry point """
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020,5,1)))

keyword = dict(
    tag=kw.lockdown,
    description=""" The Estonian government declared a state of emergency until 1 May.
                    All public gatherings were banned, including sports and cultural events;
                    schools and universities were closed; border control was restored with
                    health checks at every crossing and entry point """
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020,5,1)))

keyword = dict(
    tag=kw.close_schools,
    description=""" The Estonian government declared a state of emergency until 1 May.
                    All public gatherings were banned, including sports and cultural events;
                    schools and universities were closed; border control was restored with
                    health checks at every crossing and entry point """
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020,5,1)))

keyword = dict(
    tag=kw.close_universities,
    description=""" The Estonian government declared a state of emergency until 1 May.
                    All public gatherings were banned, including sports and cultural events;
                    schools and universities were closed; border control was restored with
                    health checks at every crossing and entry point """
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020,5,1)))

keyword = dict(
    tag="some border controls",
    description=""" The Estonian government declared a state of emergency until 1 May.
                    All public gatherings were banned, including sports and cultural events;
                    schools and universities were closed; border control was restored with
                    health checks at every crossing and entry point """
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020,5,1)))


"""
March 15:

https://news.err.ee/1064046/gyms-spas-pools-saunas-ordered-to-close
"""
begin = datetime.datetime(2020, 3, 15)
keyword = dict(
    tag=kw.close_res_bars,
    description=""" Operating bans were extended to recreation and leisure establishments,
                    ordering sports halls and clubs, gyms, pools, aqua centers, saunas, daycares,
                    and children's playrooms to be closed immediately. """
    )
measures.append(Measure(keyword, begin))


begin = datetime.datetime(2020, 3, 15)
keyword = dict(
    tag=kw.close_theaters_cinema,
    description=""" Operating bans were extended to recreation and leisure establishments,
                    ordering sports halls and clubs, gyms, pools, aqua centers, saunas, daycares,
                    and children's playrooms to be closed immediately. """
    )
measures.append(Measure(keyword, begin))

"""
March 17:
"""

begin = datetime.datetime(2020, 3, 17)
keyword = dict(
    tag="full border controls",
    description=""" Only the following people allowed to enter the country:
                    citizens of Estonia, permanent residents, their relatives,
                    and transport workers carrying out freight transport. """
    )
measures.append(Measure(keyword, begin))

"""
March 24:
"""
begin = datetime.datetime(2020, 3, 24)
keyword = dict(
    tag=kw.keep_distance,
    description=""" Government Emergency Committee decided that at least 2 meters distance
                    between people should be kept in public places, and up to two people are
                    allowed to gather in public spaces """
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 24)
keyword = dict(
    tag=kw.forbid_assemblies_all,
    description=""" Government Emergency Committee decided that at least 2 meters distance
                    between people should be kept in public places, and up to two people are
                    allowed to gather in public spaces """
    )
measures.append(Measure(keyword, begin))