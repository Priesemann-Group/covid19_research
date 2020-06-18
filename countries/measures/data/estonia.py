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
                    health checks at every crossing and entry point """,
    references="https://www.kriis.ee/en/culture-sports"
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020,5,2)))

keyword = dict(
    tag=kw.cancel_football,
    description=""" The Estonian government declared a state of emergency until 1 May.
                    All public gatherings were banned, including sports and cultural events;
                    schools and universities were closed; border control was restored with
                    health checks at every crossing and entry point """,
    references="https://www.kriis.ee/en/hobby-schools-and-trainings"
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020,5,18)))

keyword = dict(
    tag=kw.lockdown,
    description=""" The Estonian government declared a state of emergency until 1 May.
                    All public gatherings were banned, including sports and cultural events;
                    schools and universities were closed; border control was restored with
                    health checks at every crossing and entry point """,
    references="https://www.valitsus.ee/en/news/government-approved-covid-19-crisis-exit-strategy"
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020,5,2)))

keyword = dict(
    tag=kw.close_schools,
    description=""" The Estonian government declared a state of emergency until 1 May.
                    All public gatherings were banned, including sports and cultural events;
                    schools and universities were closed; border control was restored with
                    health checks at every crossing and entry point """,
    references="https://www.valitsus.ee/en/news/covid-19-crisis-exit-strategy-plan-was-published-government-committee"
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020,5,15)))

keyword = dict(
    tag=kw.close_universities,
    description=""" The Estonian government declared a state of emergency until 1 May.
                    All public gatherings were banned, including sports and cultural events;
                    schools and universities were closed; border control was restored with
                    health checks at every crossing and entry point """,
    references="https://www.kriis.ee/en/education-and-distance-learning"
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020,5,15)))

keyword = dict(
    tag="some border controls",
    description=""" The Estonian government declared a state of emergency until 1 May.
                    All public gatherings were banned, including sports and cultural events;
                    schools and universities were closed; border control was restored with
                    health checks at every crossing and entry point """
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020,5,14)))


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
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,5,2)))


begin = datetime.datetime(2020, 3, 15)
keyword = dict(
    tag=kw.close_theaters_cinema,
    description=""" Operating bans were extended to recreation and leisure establishments,
                    ordering sports halls and clubs, gyms, pools, aqua centers, saunas, daycares,
                    and children's playrooms to be closed immediately. """,
    references="https://www.kriis.ee/en/culture-sports"
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,6,1)))

"""
March 16:
"""

begin = datetime.datetime(2020, 3, 16)
keyword = dict(
    tag="full border controls",
    description=""" Only the following people allowed to enter the country:
                    citizens of Estonia, permanent residents, their relatives,
                    and transport workers carrying out freight transport. """,
    references="https://www.valitsus.ee/en/news/special-notice-estonia-eases-restrictions-border-crossings-latvia-lithuania-and-finland"
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020, 5, 14)))

"""
March 25:
"""
begin = datetime.datetime(2020, 3, 25)
keyword = dict(
    tag=kw.keep_distance,
    description=""" Government Emergency Committee decided that at least 2 meters distance
                    between people should be kept in public places, and up to two people are
                    allowed to gather in public spaces """,
    references="https://www.valitsus.ee/en/news/additional-measures-emergency-situation"
    )
measures.append(Measure(keyword, begin))

keyword = dict(
    tag="forbid assemblies > 2",
    description=""" Government Emergency Committee decided that at least 2 meters distance
                    between people should be kept in public places, and up to two people are
                    allowed to gather in public spaces """,
    references="https://www.valitsus.ee/en/news/additional-measures-emergency-situation"
    )
measures.append(Measure(keyword, begin))

"""
March 27:
"""
begin = datetime.datetime(2020, 3, 27)
keyword = dict(
    tag=kw.close_shops,
    description=""" Second, the emergency committee agreed to close shopping centres,
                    except for grocery stores, pharmacies, telecommunication outlets,
                    bank offices, parcel stations, and stores selling or renting
                    assistant and medical devices on the basis of an assistant card
                    or medical device card as of March 27. """,
    references=["https://www.valitsus.ee/en/news/additional-measures-emergency-situation",
                "https://www.valitsus.ee/en/news/special-announcement-emergency-situation-restrictions-will-be-eased-shopping-centres"
                ]
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020, 5, 11)))


"""
March 28:
"""
begin = datetime.datetime(2020, 3, 28)
keyword = dict(
    tag="Stay home if corona",
    description=""" A person infected with coronavirus
                    A person infected with coronavirus must remain at home until
                    recovery. It is forbidden to leave home or permanent residence
                    from the moment the coronavirus has been diagnosed.  The restrictions
                    on freedom of movement are essential for protecting human life
                    and health and upholding the overriding public interest in preventing
                    the spread of coronavirus causing COVID-19.
                    An infected person may only leave their home or the place of
                    stay when directed to do so by a healthcare professional or
                    the police, or in the event of an emergency endangering their
                    life or health. """,
    references="https://www.valitsus.ee/en/news/special-notice-more-restrictive-measures-saying-home-due-coronavirus"
    )
measures.append(Measure(keyword, begin))
