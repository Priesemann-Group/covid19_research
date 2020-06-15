""" # Measures for Belgium
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
March 9:
"""
begin = datetime.datetime(2020, 3, 9)
keyword = dict(
    tag=kw.cancel_football,
    description=""" all school trips were banned, all sports games were to be
                    played with no fans attending and all school championships were cancelled """,
    reference="https://www.ieidiseis.gr/ellada/item/37553-koronoios-stin-ellada-epta-nea-kroysmata-stous-73-oi-astheneis"
    )
measures.append(Measure(keyword, begin))

"""
March 10:
"""
begin = datetime.datetime(2020, 3, 10)
keyword = dict(
    tag=kw.close_schools,
    description=""" All educational institutions were closed for 14 days. Later extended to 10. May""",
    reference=[ "https://www.minedu.gov.gr/news/44308-10-03-20-prosorini-apagorefsi-tis-ekpaideftikis-leitourgias-olon-ton-ekpaideftikon-domon",
                "https://www.ekathimerini.com/251581/article/ekathimerini/news/schools-to-remain-closed-until-may-10-ministry-says"]
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020, 5, 10)))

begin = datetime.datetime(2020, 3, 10)
keyword = dict(
    tag=kw.close_universities,
    description=""" All educational institutions were closed for 14 days. Later extended to 10. May """,
    reference=[ "https://www.minedu.gov.gr/news/44308-10-03-20-prosorini-apagorefsi-tis-ekpaideftikis-leitourgias-olon-ton-ekpaideftikon-domon",
                "https://www.ekathimerini.com/251581/article/ekathimerini/news/schools-to-remain-closed-until-may-10-ministry-says"]
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020, 5, 10)))

"""
March 18:
"""
begin = datetime.datetime(2020, 3, 18)
keyword = dict(
    tag="imigrant camps restrictions",
    description=""" Greece announced new coronavirus restrictions pertaining to migrant camps.
                    For thirty days, the movement of camp residents would be restricted to small
                    groups between 7am and 7pm, which could only include one person per family and
                    would be controlled by police on public transport.
                    Specialised medical teams were sent to the camps for the creation of virus
                    isolation areas and compulsory temperature checking.
                    All other visits to the camps whether by individuals or organisations were
                    suspended for at least 14 days """,
    reference="https://web.archive.org/web/20200405061205/https://www.channelnewsasia.com/news/world/greece-unveils-new-coronavirus-restrictions-in-migrant-camps-12553024"
    )
measures.append(Measure(keyword, begin,end=datetime.datetime(2020, 3, 18)+datetime.timedelta(days=30)))

"""
March 19:
"""
begin = datetime.datetime(2020, 3, 19)
keyword = dict(
    tag=kw.forbid_assemblies_all,
    description=""" Deputy Minister of Civil Protection and Crisis Management Nikos Hardalias
                    announced a ban on public gatherings of 10 or more people and the
                    imposition of a 1,000 euro fine on violators """,
    reference="https://www.news247.gr/koinonia/koronoios-se-ischy-i-apagoreysi-synathroiseon-ano-ton-10-atomon-oi-apodektes-metakiniseis.7605395.html"
    )
measures.append(Measure(keyword, begin))


"""
March 21:
"""
begin = datetime.datetime(2020, 3, 21)
keyword = dict(
    tag="border closed",
    description=""" Deputy Minister of Civil Protection and Crisis Management Nikos Hardalias
                    announced a ban on public gatherings of 10 or more people and the
                    imposition of a 1,000 euro fine on violators """,
    reference="https://www.ethnos.gr/oikonomia/94785_koronoios-ta-metra-gia-ergazomenoys-ki-epiheiriseis"
    )
measures.append(Measure(keyword, begin))

"""
March 23:
"""
begin = datetime.datetime(2020, 3, 23)
keyword = dict(
    tag=kw.lockdown,
    description=""" Movement is permitted only for a prescribed set of reasons that include moving to or from the workplace during normal business hours,
                    shopping for food or medicine, visiting a doctor or assisting a person
                    in need of help, exercising individually or in pairs or walking a pet,
                    attending a ceremony (wedding, baptism, funeral etc.), and cases
                    of divorced parents moving to ensure communication with their children.
                    People returning to their permanent places of residence will also be exempt.
                    Citizens leaving their home are required to carry their ID or passport with them,
                    as well as some type of certification explaining the reason for their movement which has
                    to be confirmed by their employer or by themselves. """,
    reference="https://www.iefimerida.gr/ellada/apagoreysi-kykloforias-pos-tha-pate-deytera-doyleia"
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,4,27)))

keyword = dict(
    tag=kw.only_essential_travel,
    description=""" Movement is permitted only for a prescribed set of reasons that include moving to or from the workplace during normal business hours,
                    shopping for food or medicine, visiting a doctor or assisting a person
                    in need of help, exercising individually or in pairs or walking a pet,
                    attending a ceremony (wedding, baptism, funeral etc.), and cases
                    of divorced parents moving to ensure communication with their children.
                    People returning to their permanent places of residence will also be exempt.
                    Citizens leaving their home are required to carry their ID or passport with them,
                    as well as some type of certification explaining the reason for their movement which has
                    to be confirmed by their employer or by themselves. """,
    reference="https://www.iefimerida.gr/ellada/apagoreysi-kykloforias-pos-tha-pate-deytera-doyleia"
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,4,27)))

"""
March 31:
"""
begin = datetime.datetime(2020,3,31)
keyword = dict(
    tag="additional restrictiv measures",
    description=""" Deputy Minister for Civil Protection and Crisis Management Nikos Hardalias
                    announced additional restrictive measures for a duration of 14 days in the
                    municipalities of Kastoria, Orestida and Nestorio of Kastoria Regional Unit
                    as well as those of Xanthi and Myki of Xanthi Regional Unit. A night curfew
                    was imposed from 8:00 p.m. until 8:00 a.m. the following morning and some
                    options of the lockdown movement permits were suspended. Only close relatives
                    can attend a funeral and pet owners are allowed to walk their pet for up to
                    15 minutes and near their house only. """,
    reference="https://www.civilprotection.gr/el/simantika-themata/prostheta-perioristika-metra-gia-ti-metakinisi-ton-politon-stoys-dimoys-xanthis"
    )
measures.append(Measure(keyword, begin, end=begin+datetime.timedelta(days=14)))

"""
April 8:
"""
begin = datetime.datetime(2020,4,8)
keyword = dict(
    tag="roadblocks",
    description=""" The Hellenic Police installed permanent roadblocks and intensified checks
                    of vehicles in all national roads and highways across the country, as well
                    of travellers at the airports, ports, railway and bus stations. Anyone
                    travelling by car without a valid reason to a destination other than his
                    permanent residency is charged with a fine of 300 euros, is obliged to
                    return to his place of origin and the vehicle registration plates are
                    seized for 60 days. """,
    reference="https://www.civilprotection.gr/el/enimerosi-apo-ton-yfypoyrgo-politikis-prostasias-kai-diaheirisis-kriseon-niko-hardalia-kai-ton-12"
    )
measures.append(Measure(keyword, begin, end=begin+datetime.timedelta(days=14)))