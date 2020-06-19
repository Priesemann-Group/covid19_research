""" # Measures for Sweden


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
    tag="forbid assemblies > 500",
    description=""" The government bans events >500 people."""
    )
measures.append(Measure(keyword, begin))


"""
March 16:
"""
begin = datetime.datetime(2020, 3, 16)

keyword = dict(
    tag=kw.work_from_home,
    description=""" encouragement to work from home."""
    )
measures.append(Measure(keyword, begin))

keyword = dict(
    tag=kw.stay_home_if_cough,
    description=""" People even with mild symptoms are told to limit social contact."""
    )
measures.append(Measure(keyword, begin))


"""
March 18:
"""
begin = datetime.datetime(2020, 3, 18)
keyword = dict(
    tag=kw.close_schools,
    description=""" Colleges and upper secondary schools shut.
                    Reopen: The Government will remove the requirement for distance
                    education for upper secondary schools as of June 15, 2020.
                    For adult education in adult education, vocational college and
                    university and university, further education may need to be
                    given in part at a distance to reduce the spread of infection.""",
    references="https://www.krisinformation.se/detta-kan-handa/handelser-och-storningar/20192/myndigheterna-om-det-nya-coronaviruset/information-om-skolor"
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020, 6, 15)))
