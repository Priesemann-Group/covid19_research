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
    reference="https://www.irishtimes.com/news/health/coronavirus-schools-colleges-and-childcare-facilities-in-ireland-to-shut-1.4200977"
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020,3,29)))

keyword = dict(
    tag=kw.close_universities,
    description=""" Schools, colleges and childcare facilities to close. Leo Varadkar said
                    the measures being announced today would remain in place until March 29th
                    and would be kept under review.""",
    reference="https://www.irishtimes.com/news/health/coronavirus-schools-colleges-and-childcare-facilities-in-ireland-to-shut-1.4200977"
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020,3,29)))

keyword = dict(
    tag=kw.forbid_assemblies_500,
    description=""" Outdoor gatherings of more than 500 people should be cancelled""",
    reference="https://www.irishtimes.com/news/health/coronavirus-schools-colleges-and-childcare-facilities-in-ireland-to-shut-1.4200977"
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020,3,29)))

keyword = dict(
    tag="forbid indoor assemblies > 100 people",
    description=""" Outdoor gatherings of more than 500 people should be cancelled""",
    reference="https://www.irishtimes.com/news/health/coronavirus-schools-colleges-and-childcare-facilities-in-ireland-to-shut-1.4200977"
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
    reference="https://www.dublinlive.ie/news/dublin-news/coronavirus-latest-government-orders-pubs-17928776"
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
    reference="https://www.globalsecurity.org/security/library/news/2020/05/sec-200506-globaltimes05.htm"
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020, 5, 18)))

"""TODO
Look into Easing of restrictions may 5th following!
"""