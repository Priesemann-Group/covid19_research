""" # Measures for Belgium
## Stuff that might be missing:
Closure of museums
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
March 10:
"""
begin = datetime.datetime(2020, 3, 10)
keyword = dict(
    tag=kw.stay_home_if_cough,
    description=""" Everyone should stay at home if experiencing a cough or fever."""
    )
measures.append(Measure(keyword, begin))

keyword = dict(
    tag="wash hands",
    description=""" Wash your hands regularly with soap and water.""",
    references="https://www.info-coronavirus.be/en/news/protect-yourself-and-protect-the-others/"
    )
measures.append(Measure(keyword, begin))


"""
March 12:
"""
begin = datetime.datetime(2020, 3, 12)
keyword = dict(
    tag=kw.forbid_assemblies_all,
    description=""" All recreational activities cancelled regardless of size."""
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020, 5, 18)))


"""
March 14:
Official source: https://www.info-coronavirus.be/en/news/phase-2-maintained-transition-to-the-federal-phase-and-additional-measures/
"""
begin = datetime.datetime(2020, 3, 14)
keyword = dict(
    tag=kw.avoid_public_transport,
    description=""" Public transport recommended only for essential journeys """
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 14)
keyword = dict(
    tag=kw.work_from_home,
    description=""" work from home encouraged """
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 14)
keyword = dict(
    tag=kw.close_res_bars,
    description=""" all public places e.g. restaurants closed """,
    references="https://www.info-coronavirus.be/en/news/nsc-0306/"
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020, 6, 8)))

begin = datetime.datetime(2020, 3, 14)
keyword = dict(
    tag=kw.close_shops,
    description=""" all public places e.g. restaurants closed """,
    references="https://www.info-coronavirus.be/en/news/nsc-6-05/"
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020, 5, 11)))

begin = datetime.datetime(2020, 3, 14)
keyword = dict(
    tag=kw.close_theaters_cinema,
    description=""" all public places e.g. restaurants closed """,
    references="https://www.info-coronavirus.be/en/news/nsc-0306/"
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020, 7, 1)))

"""
March 16:
(as March 14 was a Saturday)
"""
begin = datetime.datetime(2020, 3, 16)
keyword = dict(
    tag=kw.close_schools,
    description=""" Nationwide school closures.""",
    references="https://www.info-coronavirus.be/en/news/nsc-13-05/"
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020, 5, 18)))

"""
March 18:
"""
begin = datetime.datetime(2020, 3, 18)
keyword = dict(
    tag=kw.lockdown,
    description=""" Citizens are required to stay at home except for work and
                    essential journeys. Going outdoors only with household
                    members or 1 friend.""",
    references="https://www.info-coronavirus.be/en/news/nsc-6-05/"
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020, 5, 10)))

begin = datetime.datetime(2020, 3, 18)
keyword = dict(
    tag=kw.case_based_isolation,
    description=""" Implemented at lockdown."""
    )
measures.append(Measure(keyword, begin))


"""
May 11:
"""
begin = datetime.datetime(2020, 5, 11)
keyword = dict(
    tag="restricted entry to shops",
    description=""" On the 11th of May we will also reopen the shops. Shops will
                    only be allowed to reopen - as always - if they can strictly
                    comply with the following rules:
                    For the shops that are already open - only 1 customer per 10m²
                    will be allowed, for a maximum of 30 minutes. An exception is
                    made for smaller shops.
                    Customers are strongly recommended to wear protection that covers
                    the nose and mouth when inside a store. In any case, a safe
                    distance must be kept.
                    Employers are responsible for the health and safety of their
                    employees and must make every effort to ensure safe working
                    conditions.
                    To avoid overcrowding, people will have to do their shopping
                    alone. An exception is made for children under the age of 18
                    - they can be accompanied by a parent - and for people who require
                    assistance. We also recommend that you frequent shops that are
                    located in a city or town near your home or workplace. """,
    references="https://www.info-coronavirus.be/en/news/nsc-6-05/"
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020, 5, 11)))

"""
May 18:
"""
begin = datetime.datetime(2020, 5, 18)
keyword = dict(
    tag="forbid assemblies > 30",
    description=""" Regular outdoor group sports training and lessons may resume,
                    provided social distancing is adhered to and a coach is present.
                    Groups may not exceed 20 persons and sports clubs may re-open
                    only on condition that all possible measures are taken to guarantee
                    the safety of the sportsmen and sportswomen. With regard to
                    weddings and funerals, a maximum of 30 people will be allowed
                    to attend from 18 May under certain conditions, such as respecting
                    social distancing. However, it is not permitted to organise
                    a reception after the ceremony.""",
    references="https://www.info-coronavirus.be/en/news/nsc-13-05/"
    ) # technically below is also forbidden. Context-independent (until 10 people) is only allowed after June 8
measures.append(Measure(keyword, begin, end=datetime.datetime(2020, 5, 18)))
