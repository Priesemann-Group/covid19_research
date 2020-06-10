""" # Measures for the czech republic
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
[wikpedia](https://en.wikipedia.org/wiki/COVID-19_pandemic_in_the_Czech_Republic#Policies_to_fight_the_contagion)
"""
measures = []  # Create empty array on which we append later on

"""
Recreating every entry from the wikipedia table
"""
begin = datetime.datetime(2020, 1, 30)
keyword = dict(
    tag="suspending new china visa",
    description=""" Suspension of issuing of new visas in China.  """,
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,4,21)))

begin = datetime.datetime(2020, 2, 9)
keyword = dict(
    tag="no flights china",
    description=""" Suspension of direct flights to/from China. """,
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,4,21)))

begin = datetime.datetime(2020, 3, 5)
keyword = dict(
    tag=kw.restrict_travel_italy,
    description=""" Suspension of direct flights to/from selected regions of Italy. """,
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,3,19)))

begin = datetime.datetime(2020, 3, 5)
keyword = dict(
    tag="no flights korea",
    description=""" Suspension of direct flights to/from South Korea.  """,
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,3,24)))

begin = datetime.datetime(2020, 3, 7)
keyword = dict(
    tag="suspending new iran visa",
    description=""" Suspension of issuing of new visas in Iran. """,
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,4,21)))

begin = datetime.datetime(2020, 3, 9)
keyword = dict(
    tag="more border control",
    description=""" Random medical checks at major border crossings  """,
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 4)
keyword = dict(
    tag="FFP3 respirators sale ban",
    description=""" The FFP3 respirators sale ban was preceded by a memo from
                    Security Information Service to the Government, according to
                    which Chinese embassy in Prague was conducting massive
                    purchases of respirators available on Czech market during January
                    and February and transferring them to China.   

                    This led to shortage of FFP3 respirators for use by healthcare
                    providers which lasted for weeks after the ban was passed. """,
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,4,6)))

begin = datetime.datetime(2020, 3, 5)
keyword = dict(
    tag="Hand sanitizers export ban",
    description=""" Ban on export of hand sanitizers listed in Annex 1,
                    Category 1 of EU Regulation No. 528/2012 (with exemption
                    of small amounts for personal use). """,
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,4,21)))

begin = datetime.datetime(2020, 3, 5)
keyword = dict(
    tag="Ban on export of medication",
    description=""" 17 March – 1 April 2020 – general ban on export of medication.
                    From 1 April onwards – ban on export of selected medication.

                    Ban only on export of medication destined for the Czech market.
                    Medication manufactured directly to foreign order may still be exported. """,
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 4)
keyword = dict(
    tag="Duty to report gatherings over 5,000 people",
    description=""" Organisers must inform health authorities about all planned
                    gatherings where they expect 5,000 or more visitors during a single day  """,
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,4,17)))

begin = datetime.datetime(2020, 3, 9)
keyword = dict(
    tag="No spectators biathlon",
    description=""" Spectators banned from attending the World Biathlon Cup
                    Championship race in Nové Město na Moravě.   """,
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 4, 14)
keyword = dict(
    tag="self-quarantine",
    description=""" Residents returning from abroad ordered to self-quarantine for 14 days. """,
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 19)
keyword = dict(
    tag="Contact tracing",
    description=""" Use of mobile phone geolocation data and debit card payments for contact tracing. """,
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 10)
keyword = dict(
    tag="Hospital visits ban",
    description=""" Ban on visits in hospitals and similar facilities. Exemptions for visits 
                    to patients who are (1) minors, (2) legally incapacitated, (3) pregnant or (4) terminally ill. """,
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 10)
keyword = dict(
    tag="forbid assemblies > 100 people",
    description=""" Gatherings of 100 or more people banned. """,
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,4,17)))

begin = datetime.datetime(2020, 3, 13)
keyword = dict(
    tag="forbid assemblies > 30 people",
    description=""" Gatherings of 30 or more people banned. Revoked from 16 March onwards
                    (replaced by nationwide curfew, see below). """,
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,3,16)))

begin = datetime.datetime(2020, 3, 23)
keyword = dict(
    tag=kw.forbid_assemblies_all,
    description=""" Gatherings of more than 2 people banned. """,
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,4,27)))

begin = datetime.datetime(2020, 4, 24)
keyword = dict(
    tag="forbid assemblies > 10 people",
    description=""" Gatherings of more than 10 people banned. """,
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 5, 25)
keyword = dict(
    tag="forbid assemblies > 300 people",
    description=""" Gatherings of 300 or more people banned. """,
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 11)
keyword = dict(
    tag=kw.close_schools,
    description=""" All pupils and students banned from personally attending classes
                    (including university lectures). Staff may continue to work and assign
                    homework for students.

                    Kindergartens and creches are open/closed subject to decision of local
                    municipal authorities. """,
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 11)
keyword = dict(
    tag=kw.close_universities,
    description=""" All pupils and students banned from personally attending classes
                    (including university lectures). Staff may continue to work and assign
                    homework for students.

                    Kindergartens and creches are open/closed subject to decision of local
                    municipal authorities. """,
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 14)
keyword = dict(
    tag=kw.close_res_bars,
    description=""" All publicly accessible restaurants closed.

                    Restaurants may sell food through shopfront windows with any opening hours (incl. 24/7),
                    so long as customers do not enter the premises.

                    Home delivery possible 24/7.

                    From 11 May: Restaurants may serve patrons at their outdoors premises.

                    From 25 May: Restaurants may operate from 6 AM to 23 PM (outdoor premises, take away windows
                    and home delivery 24/7). """,
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 14)
keyword = dict(
    tag=kw.close_theaters_cinema,
    description=""" All shops closed """,
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,5,11)))

begin = datetime.datetime(2020, 3, 14)
keyword = dict(
    tag=kw.close_shops,
    description=""" All shops closed """,
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,5,11)))

begin = datetime.datetime(2020, 3, 14)
keyword = dict(
    tag="Prison visits ban",
    description=""" Family members banned from visiting relatives in prisons and jails.
                    Defense attorneys exempted from the ban. Individual exceptions may be 
                    granted by the Minister of Justice.
                    From 15 May onwards: Only one visitor permitted per each visit. """,
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 13)
keyword = dict(
    tag="Sporting venues closed",
    description=""" Public banned from entering sporting venues for 30 or more people,
                    both indoor and outdoor. """,
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 29)
keyword = dict(
    tag="Welfare providers and retirement homes can accept new clients only after negative COVID-19 test",
    description=""" This includes also clients that are moved from another institution
                    (another retirement home).
                    Until 25 May: Once accepted, the person must be placed at a separate
                    room for 14 days. """,
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 15)
keyword = dict(
    tag=kw.lockdown,
    description=""" NATIONWIDE CURFEW """,
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,4,24)))


begin = datetime.datetime(2020, 3, 19)
keyword = dict(
    tag="Obligatory face cover",
    description=""" Obligatory face cover (respirator or similar) """,
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 19)
keyword = dict(
    tag="Elderly shopping time ",
    description=""" Elderly only shopping time (65+) """,
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 19)
keyword = dict(
    tag=kw.forbid_assemblies_all,
    description=""" Local Assemblies limited """,
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 16)
keyword = dict(
    tag="close border",
    description=""" COMPLETE BORDERS CLOSURE
                    Czech citizens:
                    Not allowed to leave the country unless they have long-term or permanent residency abroad.
                    May return to the country; subject to mandatory 14 days' self-quarantine (see above).
                    Foreigners with long-term or permanent residency:
                    Allowed to leave the country.
                    May return to the country if they were outside when measure adopted; subject to mandatory 14 days' self-quarantine (see above).
                    May not return to the country if left while the measure was in force.
                    Foreigners without long-term or permanent residency:
                    Allowed to leave the country.
                    Not allowed to enter the country.""",
    )
measures.append(Measure(keyword, begin))
