""" # Measures for Republic of Ireland
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
[Reopening phases](https://www.gov.ie/en/publication/b07ffe-reopening-business-elements/)
[wikipedia](https://en.wikipedia.org/wiki/COVID-19_pandemic_in_the_Republic_of_Ireland#Timeline)
"""
measures = []  # Create empty array on which we append later on

"""
March 12:
"""
begin = datetime.datetime(2020, 3, 12)
keyword = dict(
    tag=kw.close_schools,
    description=""" Schools, colleges and childcare facilities to close. Leo Varadkar said
                    the measures being announced today would remain in place until March 29th
                    and would be kept under review.""",
    references="https://www.irishtimes.com/news/health/coronavirus-schools-colleges-and-childcare-facilities-in-ireland-to-shut-1.4200977"
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020,3,29)))

keyword = dict(
    tag=kw.close_universities,
    description=""" Schools, colleges and childcare facilities to close. Leo Varadkar said
                    the measures being announced today would remain in place until March 29th
                    and would be kept under review.""",
    references="https://www.irishtimes.com/news/health/coronavirus-schools-colleges-and-childcare-facilities-in-ireland-to-shut-1.4200977"
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020,3,29)))

keyword = dict(
    tag=kw.forbid_assemblies_500,
    description=""" Outdoor gatherings of more than 500 people should be cancelled""",
    references="https://www.irishtimes.com/news/health/coronavirus-schools-colleges-and-childcare-facilities-in-ireland-to-shut-1.4200977"
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020,3,29)))

keyword = dict(
    tag="forbid indoor assemblies > 100 people",
    description=""" Outdoor gatherings of more than 500 people should be cancelled""",
    references="https://www.irishtimes.com/news/health/coronavirus-schools-colleges-and-childcare-facilities-in-ireland-to-shut-1.4200977"
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020,3,29)))

"""
March 15:
"""
begin = datetime.datetime(2020, 3, 15)
keyword = dict(
    tag=kw.close_res_bars,
    description=""" Following discussions today with the Licenced Vintners Association (LVA) and
                    the Vintners Federation of Ireland (VFI), the Government is now calling on
                    all public houses and bars (including hotel bars) to close from this evening
                    (Sunday 15 March) until at least 29 March""",
    references="https://www.dublinlive.ie/news/dublin-news/coronavirus-latest-government-orders-pubs-17928776"
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020, 3, 29)))

"""
March 27:
"""
begin = datetime.datetime(2020, 3, 27)
keyword = dict(
    tag=kw.lockdown,
    description=""" The government issued a stay-at-home order, demanding all the people in
                    the country not to leave their homes unless in some specific circumstances,
                    such as going outside for the government-defined essential work or for
                    buying food or medicine.
                    The order, which was supposed to come to an end on Tuesday,
                    has been extended for two more weeks until May 18 except the above-mentioned
                    two minor changes due to the fact that the pandemic still poses a serious threat
                    to public health.""",
    references="https://www.globalsecurity.org/security/library/news/2020/05/sec-200506-globaltimes05.htm"
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020, 5, 18)))

keyword = dict(
    tag=kw.close_shops,
    description=""" As part of lockdown. (assumed)
                    Reopen: All retail is reopening. Shop locally, shop safely
                    and support businesses in your community.""",
    references="https://www.gov.ie/en/publication/7ae99f-easing-the-covid-19-restrictions-on-june-8-phase-2/"
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020, 6, 8)))

"""
May 18:
[Government publication for phase 1 of easing the restrictions]
(https://www.gov.ie/en/publication/ad5dd0-easing-the-covid-19-restrictions-on-may-18-phase-1/)
"""
begin = datetime.datetime(2020, 5, 18)
keyword = dict(
    tag="stay home",
    description=""" You should still stay at home as much as you possibly can."""
    )
measures.append(Measure(keyword, begin))

keyword = dict(
    tag="no spontaneous gatherings > 4",
    description=""" Up to 4 people who don't live together can meet outdoors
                    while keeping at least 2 metres apart."""
    )
measures.append(Measure(keyword, begin))


"""
June 8:
[Government publication for phase 2 of easing the restrictions]
(https://www.gov.ie/en/publication/7ae99f-easing-the-covid-19-restrictions-on-june-8-phase-2/)
"""
begin = datetime.datetime(2020, 6, 8)
keyword = dict(
    tag="stay local",
    description=""" Stay Local: You may travel within your own county, or up to
                    20 kilometres from your home if crossing county boundaries."""
    )
measures.append(Measure(keyword, begin))

keyword = dict(
    tag="no spontaneous gatherings > 15",
    description=""" Meeting other people: You may meet up to 6 people from outside
                    your household both indoors and outdoors for social gatherings.
                    Organised outdoor exercise, sporting, cultural or social activities
                    of up to 15 people may take place."""
    )
measures.append(Measure(keyword, begin))

"""
Next reopening phase starts June 29
"""
