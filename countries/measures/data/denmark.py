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
measures.append(Measure(keyword, begin, end=datetime.datetime(2020, 3, 18)))

begin = datetime.datetime(2020, 3, 12)
keyword = dict(
    tag=kw.close_theaters_cinema,
    description=""" closed cultural institutions, leisure facilities etc """,
    references="https://www.regeringen.dk/nyheder/2020/aftale-om-yderligere-genaabning-i-fase-2/"
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020, 5, 27)))

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
                    (primary schools also shut on 16th).""",
    references="https://www.regeringen.dk/nyheder/2020/pressemoede-om-genaabning-af-danmark-fase-2/"
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020, 5, 18)))

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
                    (primary schools also shut on 16th).""",
    references="https://www.regeringen.dk/nyheder/2020/genaabning-af-skoler-og-dagstilbud/"
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020, 4, 15)))


"""
March 18:
"""
begin = datetime.datetime(2020, 3, 18)
keyword = dict(
    tag=kw.lockdown,
    description=""" Bans of gatherings of >10 people in public and all public
                    places were shut.""",
    references="https://www.regeringen.dk/nyheder/2020/genaabning-af-skoler-og-dagstilbud/"
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020, 4, 11)))

keyword = dict(
    tag=kw.close_shops,
    description=""" As part of the lockdown.
                    Reopening: Full opening of retail (May 11)
                    Retail - including major centers - can reopen under the guidelines
                    agreed in the Sectoral Partnership - in light of the outbreak
                    of COVID-19 ”. (Translated from Danish)""",
    references="https://www.regeringen.dk/nyheder/2020/pressemoede-om-genaabning-af-danmark-fase-2/"
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020, 5, 11)))

keyword = dict(
    tag=kw.close_res_bars,
    description=""" As part of the lockdown.
                    Reopening: Restaurant and café life and the like. commences (May 18)
                    Restaurants, cafes and the like. can serve under more detailed
                    guidelines including regarding opening hours, physical distance,
                    etc. (Translated from Danish)""",
    references="https://www.regeringen.dk/nyheder/2020/pressemoede-om-genaabning-af-danmark-fase-2/"
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020, 5, 18)))

"""
April 20:
"""
begin = datetime.datetime(2020, 4, 20)
keyword = dict(
    tag="Reopen courts, liberal professions, ...",
    description=""" Liberal professions
                    As part of the effort against COVID-19, a temporary ban on hairdressers
                    and certain liberal professions has been introduced, cf. Executive
                    Order on Prohibition of Larger Assemblies and on Access to and
                    Restrictions on Premises in Covid-19 Handling. At the same time,
                    a temporary ban on practical driving lessons in school cars
                    was introduced. The bans will be repealed with effect from Monday,
                    April 20, 2020, enabling traders to re-open their premises to
                    customers, as well as practical driving lessons in school vehicles.
                    A sectoral partnership is established where the relevant authorities,
                    together with industries, trade unions and relevant organizations,
                    agree on guidelines for responsible reopening.
                    Companies that have been closed down may consider that it is
                    not appropriate to close up. In this situation, a company that
                    has previously been subject to a ban and has therefore been
                    closed can choose to continue to be closed and will then receive
                    up to 80 per cent under the current scheme. in compensation
                    for the fixed expenses.
                    The reopening of the courts, etc.
                    The Danish Courts have initiated emergency preparedness to handle
                    critical cases, but far more cases are needed. The courts are
                    therefore urged to reopen in order to be able to complete as
                    many cases as possible. At the same time, the Family Court House
                    will open for conducting child interviews and supervised attendance
                    as very specific child-related critical activities.
                    As health care is judged to be sound, a call for imprisonment
                    in the Prison Service is gradually started.
                    A partial reopening of research laboratories for researchers
                    and students will be carried out. will be able to continue and
                    complete post-doc or PhD courses as well as continue research
                    experiments and research projects that are otherwise lost.
                    A sectoral partnership is established for each of the above
                    tracks, where guidelines for responsible reopening are agreed.""",
    references="https://www.regeringen.dk/nyheder/2020/aftale-vedroerende-udvidelse-af-den-foerste-fase-af-en-kontrolleret-genaabning/"
    )
measures.append(Measure(keyword, begin))


"""
May 27:
"""
begin = datetime.datetime(2020, 5, 27)
keyword = dict(
    tag="Reopen university life",
    description=""" Details see reference""",
    references = "https://www.regeringen.dk/nyheder/2020/aftale-om-yderligere-genaabning-i-fase-2/"
    )
measures.append(Measure(keyword, begin))


"""
June 8:
"""
begin = datetime.datetime(2020, 3, 12)
keyword = dict(
    tag="ban assemblies > 50",
    description=""" As of today, the limit is 50 people. (Translated from Danish)""",
    references = "https://www.regeringen.dk/nyheder/2020/forsamlingsforbuddet-bliver-lempet/"
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020, 7, 8)))
