""" # Measures for Finland
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
March 16:

https://news.err.ee/1063224/estonian-government-declares-emergency-situation-against-coronavirus
"""

begin = datetime.datetime(2020, 3, 16)
keyword = dict(
    tag=kw.forbid_assemblies_all,
    description=""" The Finnish Government, in cooperation with the President of Finland,
                    declared a state of emergency in the country. A list of measures intended
                    to slow down the spreading of the virus and to protect at-risk groups
                    were implemented in accordance with the Emergency Powers Act (1552/2011),
                    the Communicable Diseases Act (1227/2016), and other legislation.
                    The measures include the closing of schools (excluding early education)
                    and most government-run public facilities, limiting public gatherings,
                    and closing the country's borders.
                    The restrictions were scheduled to last until 13 April, but in late
                    March they were extended to 13 May. """
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020,5,13)))


keyword = dict(
    tag=kw.close_schools,
    description=""" The Finnish Government, in cooperation with the President of Finland,
                    declared a state of emergency in the country. A list of measures intended
                    to slow down the spreading of the virus and to protect at-risk groups
                    were implemented in accordance with the Emergency Powers Act (1552/2011),
                    the Communicable Diseases Act (1227/2016), and other legislation.
                    The measures include the closing of schools (excluding early education)
                    and most government-run public facilities, limiting public gatherings,
                    and closing the country's borders.
                    The restrictions were scheduled to last until 13 April, but in late
                    March they were extended to 13 May. """
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020,5,13)))

keyword = dict(
    tag=kw.close_universities,
    description=""" The Finnish Government, in cooperation with the President of Finland,
                    declared a state of emergency in the country. A list of measures intended
                    to slow down the spreading of the virus and to protect at-risk groups
                    were implemented in accordance with the Emergency Powers Act (1552/2011),
                    the Communicable Diseases Act (1227/2016), and other legislation.
                    The measures include the closing of schools (excluding early education)
                    and most government-run public facilities, limiting public gatherings,
                    and closing the country's borders.
                    The restrictions were scheduled to last until 13 April, but in late
                    March they were extended to 13 May. """
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020,5,13)))

keyword = dict(
    tag=kw.lockdown,
    description=""" The Finnish Government, in cooperation with the President of Finland,
                    declared a state of emergency in the country. A list of measures intended
                    to slow down the spreading of the virus and to protect at-risk groups
                    were implemented in accordance with the Emergency Powers Act (1552/2011),
                    the Communicable Diseases Act (1227/2016), and other legislation.
                    The measures include the closing of schools (excluding early education)
                    and most government-run public facilities, limiting public gatherings,
                    and closing the country's borders.
                    The restrictions were scheduled to last until 13 April, but in late
                    March they were extended to 13 May. """
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020,5,13)))

keyword = dict(
    tag="border closed",
    description=""" The Finnish Government, in cooperation with the President of Finland,
                    declared a state of emergency in the country. A list of measures intended
                    to slow down the spreading of the virus and to protect at-risk groups
                    were implemented in accordance with the Emergency Powers Act (1552/2011),
                    the Communicable Diseases Act (1227/2016), and other legislation.
                    The measures include the closing of schools (excluding early education)
                    and most government-run public facilities, limiting public gatherings,
                    and closing the country's borders.
                    The restrictions were scheduled to last until 13 April, but in late
                    March they were extended to 13 May. """
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020,5,13)))