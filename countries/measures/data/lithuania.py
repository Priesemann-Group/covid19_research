""" # Measures for Lithuania
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

[wikipedia](https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Greece)
"""
measures = []  # Create empty array on which we append later on

"""
Feb 28:
"""
begin = datetime.datetime(2020, 2, 28)
keyword = dict(
    tag="cancel public events",
    description="""  Seimas cancelled all public events on its premises until 30 April. """,
    reference="https://www.lrs.lt/sip/portal.show?p_r=35403&p_k=1&p_t=270150&p6=27"
    )
measures.append(Measure(keyword, begin))

"""
March 12:
"""
begin = datetime.datetime(2020, 3, 12)
keyword = dict(
    tag=kw.close_schools,
    description=""" On the same day, the government ordered the closure of all educational
                    institutions including kindergartens, public schools,
                    and universities for two weeks with a recommendation to utilise online learning.""",
    reference="http://lrv.lt/lt/naujienos/visoje-lietuvoje-del-koronaviruso-dviem-savaitems-uzdaromos-svietimo-istaigos"
    )
measures.append(Measure(keyword, begin, end=begin+datetime.timedelta(days=14)))

keyword = dict(
    tag=kw.close_universities,
    description=""" On the same day, the government ordered the closure of all educational
                    institutions including kindergartens, public schools,
                    and universities for two weeks with a recommendation to utilise online learning.""",
    reference="http://lrv.lt/lt/naujienos/visoje-lietuvoje-del-koronaviruso-dviem-savaitems-uzdaromos-svietimo-istaigos"
    )
measures.append(Measure(keyword, begin, end=begin+datetime.timedelta(days=14)))

keyword = dict(
    tag=kw.close_theaters_cinema,
    description=""" All museums, cinemas, and gyms were also closed. """,
    reference="https://www.lrt.lt/naujienos/lietuvoje/2/1150971/nuo-penktadienio-del-koronaviruso-gresmes-nebedirbs-dalis-ugdymo-istaigu-atsaukiami-kulturiniai-sporto-renginiai"
    )
measures.append(Measure(keyword, begin))


"""
March 16:
"""
begin = datetime.datetime(2020, 3, 16)
end = datetime.datetime(2020, 6, 17)

description_march_16 = """ Lithuania was put under quarantine. All public indoor and outdoor gatherings were prohibited;
                    all shops and businesses excluding grocery shops, pharmacies and veterinary pharmacies were closed;
                    all restaurants and bars were closed, leaving the option for food take-away; borders were closed for
                    foreigners regardless of the means of transport, excluding cargo and special transport;
                    all international outbound passenger travel was prohibited.
                    The quarantine was set to last until 30 March, but later revised to 17. Jun"""

references_march_16 = ["https://www.lrt.lt/naujienos/lietuvoje/2/1151427/skvernelis-pranese-kad-sestadieni-bus-priimtas-sprendimas-del-karantino-salies-mastu","https://www.lrt.lt/en/news-in-english/19/1187146/lithuania-decides-to-lift-quarantine"]
keyword = dict(
    tag=kw.lockdown,
    description=description_march_16,
    reference=references_march_16
    )
measures.append(Measure(keyword, begin,end=end))

keyword = dict(
    tag=kw.forbid_assemblies_all,
    description=description_march_16,
    reference=references_march_16
    )
measures.append(Measure(keyword, begin,end=end))

keyword = dict(
    tag=kw.close_res_bars,
    description=description_march_16,
    reference=references_march_16
    )
measures.append(Measure(keyword, begin,end=end))

keyword = dict(
    tag=kw.close_shops,
    description=description_march_16,
    reference=references_march_16
    )
measures.append(Measure(keyword, begin,end=end))

keyword = dict(
    tag=kw.close_theaters_cinema,
    description=description_march_16,
    reference=references_march_16
    )
measures.append(Measure(keyword, begin,end=end))

keyword = dict(
    tag="border closed",
    description=description_march_16,
    reference=references_march_16
    )
measures.append(Measure(keyword, begin,end=end))
