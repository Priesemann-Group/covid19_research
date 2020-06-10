""" # Measures for the Netherlands

We look at the different measures as can be seen on the [Wikipedia timeline](...) and ref....
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
[dutchnews.nl](https://www.dutchnews.nl/news/2020/05/coronavirus-a-timeline-of-the-pandemic-in-the-netherlands/)
"""
measures = []  # Create empty array on which we append later on

"""
March 6:
The RIVM advises people in Noord-Brabant who have cold-like
symptoms to stay home until they recover.
"""
begin = datetime.datetime(2020, 3, 6)
keyword = dict(
    tag=kw.stay_home_if_cough,
    description=""" On March 6 the RIVM advises people in Noord-Brabant who have cold-like
                    symptoms to stay home until they recover. """,
    )
measures.append(Measure(keyword, begin))


"""
March 9:
"""
begin = datetime.datetime(2020, 3, 9)
keyword = dict(
    tag="ban on hand shaking",
    description=""" Rutte announces a ban on hand shaking and advises people in Noord-Brabant
                    to work from home if possible for the next seven days.
                    The Netherlands is still in the containment phase, he says. """,
    )
measures.append(Measure(keyword, begin))


"""
March 10:
"""
begin = datetime.datetime(2020, 3, 10)
keyword = dict(
    tag=kw.restrict_travel_italy,
    description=""" The Dutch government changes its travel advice to Italy to code orange,
                    meaning essential travel only.""",
    )
measures.append(Measure(keyword, begin))

"""
March 12:
"""
begin = datetime.datetime(2020, 3, 12)
keyword = dict(
    tag="work from home guideline",
    description=""" The ‘work from home guideline’ is extended to the whole country."""
    )
measures.append(Measure(keyword, begin))
keyword = dict(
    tag="forbid assemblies > 100 people",
    description=""" Gatherings of more than 100 people are banned. Rutte refuses to
                    close schools despite pressure from teachers, insisting children are
                    ‘not a big risk group’."""
    )
measures.append(Measure(keyword, begin))
keyword = dict(
    tag = kw.cancel_football,
    description=""" The KNVB cancels all domestic football matches also sometimes quoted to start at
                    the 8 March"""
    )
measures.append(Measure(keyword, begin))


"""
March 15:
"""
begin = datetime.datetime(2020, 3, 15)
keyword = dict(
    tag="lockdown",
    description=""" The ‘intelligent lockdown’ in the Netherlands begins. Rutte gives in to
                    pressure to close schools until April 6 """
    )
measures.append(Measure(keyword, begin))
keyword = dict(
    tag="close schools",
    description=""" The ‘intelligent lockdown’ in the Netherlands begins. Rutte gives in to
                    pressure to close schools until April 6 """
    )
measures.append(Measure(keyword, begin))
keyword = dict(
    tag="close restaurants and bars",
    description=""" Cafes, restaurants, sports and sex clubs are given less than an hour’s
                    notice to close. """
    )
measures.append(Measure(keyword, begin))
keyword = dict(
    tag = kw.keep_distance,
    description=""" People are instructed to keep 1.5 metres apart at all times. """
    )
measures.append(Measure(keyword, begin))


"""
March 17:
"""
begin = datetime.datetime(2020, 3, 17)
keyword = dict(
    tag=kw.only_essential_travel,
    description=""" The foreign affairs ministry changes travel advice for all countries to code
                    orange (essential journeys only) until April 6. EU member states agree to close
                    their external borders for 30 days. """
    )
measures.append(Measure(keyword, begin))
keyword = dict(
    tag="scaled down raile timetable",
    description=""" Rail operator NS says a scaled-down timetable will run from Saturday,
                    with night trains and most inter-city services cancelled. """
    )
measures.append(Measure(keyword, begin))

"""
March 18:
"""
begin = datetime.datetime(2020, 3, 18)
keyword = dict(
    tag=kw.close_schools,
    description=""" Education minister Arie Slob cancels end-of-year exams for children
                    in the last year of primary school. """
    )
measures.append(Measure(keyword, begin))


"""
March 23:
"""
begin = datetime.datetime(2020, 3, 23)
keyword = dict(
    tag=kw.forbid_assemblies_all,
    description=""" Groups of more than three people in public are banned and mayors are
                    given powers to clear public spaces. """)
measures.append(Measure(keyword, begin))

keyword = dict(
    tag=kw.close_shops,
    description=""" ‘Contact professions’ such as hairdressers, nail studios,
                    tattoo parlours and physiotherapists are ordered to close. """
    )
end = datetime.datetime(2020, 5, 11)
measures.append(Measure(keyword, begin, end))


"""
May 5:
"""
begin = datetime.datetime(2020, 5, 5)
keyword = dict(
    tag=kw.demonstration_start,
    description=""" Liberation Day is celebrated with no public events.
                    A small number of protesters stage ‘Stop the Lockdown’ demonstrations
                    in The Hague and Utrech """
    )
measures.append(Measure(keyword, begin))


"""
May 11:
"""
begin = datetime.datetime(2020, 5, 11)
keyword = dict(
    tag="primary schools ban parents from playground",
    description=""" Primary schools ban parents from the playground and introduce one-way systems to
                    maintain the 1.5 metre rule. Most pupils are attending school two days a week. """
    )
measures.append(Measure(keyword, begin))
