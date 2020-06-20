""" # Measures for Switzerland
TODO:
* Do not have measures such as closing of museums yet.
* Need to add ends/begins of different kinds of assemblies.
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
[wikipedia](https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Switzerland)
[Ferguson et al. March 2020](https://www.imperial.ac.uk/mrc-global-infectious-disease-analysis/covid-19/report-13-europe-npi-impact/)
"""
measures=[]

"""
February 28:
"""
begin = datetime.datetime(2020, 2, 28)
keyword = dict(
    tag=kw.forbid_assemblies_1000,
    description=""" The Federal Council banned events involving more than
                    1,000 people in an effort to curb the spread of the infection. """
)
measures.append(Measure(keyword, begin))


"""
March 2:
"""
begin = datetime.datetime(2020, 3, 2)
keyword = dict(
    tag=kw.stay_home_if_cough,
    description=""" Advice to self-isolate if experiencing a cough or fever symptoms. """
)
measures.append(Measure(keyword, begin))


"""
March 14:
"""
begin = datetime.datetime(2020, 3, 14)
keyword = dict(
    tag=kw.close_schools,
    description=""" The Federal Council decided to cancel classes in all educational
                    establishments.
                    Reopen: Geöffnet/gestattet seit 11. Mai
                    Präsenzunterricht in obligatorischen Schulen (Primar- und Sekundarschulen I)
                    Präsenzunterricht mit maximal 5 Personen (einschliesslich Lehrperson) an Schulen der Sekundarstufe II, der Tertiärstufe sowie weiteren Ausbildungsstätten (Fahrschule, Sprachkurse)
                    Prüfungen in Ausbildungsstätten """,
    references="https://www.bag.admin.ch/bag/de/home/krankheiten/ausbrueche-epidemien-pandemien/aktuelle-ausbrueche-epidemien/novel-cov/massnahmen-des-bundes.html#1055950590"
)
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,5,11)))

keyword = dict(
    tag=kw.close_universities,
    description=""" The Federal Council decided to cancel classes in all educational
                    establishments.
                    Reopen: Geöffnet/gestattet seit 6. Juni
                    Präsenzunterricht in den Mittel-, Berufs- und Hochschulen sowie weiteren Ausbildungsstätten """,
    references="https://www.bag.admin.ch/bag/de/home/krankheiten/ausbrueche-epidemien-pandemien/aktuelle-ausbrueche-epidemien/novel-cov/massnahmen-des-bundes.html#1055950590"
)
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,6,6)))

keyword = dict(
    tag="forbid assemblies > 100 people",
    description=""" The Federal Council has banned all events (public or private) involving
                    more than 100 people. """
)
measures.append(Measure(keyword, begin)) #TODO Technically you can have larger gatherings to 300 already...

keyword = dict(
    tag="border closed",
    description=""" The Federal Council has also decided to partially close
                    its borders and enacted border controls.
                    Reopen: Geöffnet seit 15. Juni
                    Grenze zu allen EU-/EFTA-Staaten und UK """,
    references="https://www.bag.admin.ch/bag/de/home/krankheiten/ausbrueche-epidemien-pandemien/aktuelle-ausbrueche-epidemien/novel-cov/massnahmen-des-bundes.html#1055950590"
)
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,6,15)))

"""
March 16:
"""
begin = datetime.datetime(2020, 3, 16)
keyword = dict(
    tag=kw.close_shops,
    description=""" The Federal Council announced further measures, include the
                    closure of bars, shops and other gathering places.
                    Reopen: Geöffnet/gestattet seit 11. Mai
                    Einkaufsläden und Märkte""",
    references="https://www.bag.admin.ch/bag/de/home/krankheiten/ausbrueche-epidemien-pandemien/aktuelle-ausbrueche-epidemien/novel-cov/massnahmen-des-bundes.html#accordion1592594518906"
)
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,5,11)))

keyword = dict(
    tag=kw.close_res_bars,
    description=""" The Federal Council announced further measures, include the
                    closure of bars, shops and other gathering places.
                    Reopen: Geöffnet/gestattet seit 11. Mai
                    Besuch von Gastronomiebetrieben unter folgenden Bedingungen:
                    die einzelnen Gästegruppen bestehen aus maximal 4 Personen oder
                    Eltern mit Kindern (auch Patchwork-Familien), die Konsumation
                    erfolgt ausschliesslich sitzend""",
    references="https://www.bag.admin.ch/bag/de/home/krankheiten/ausbrueche-epidemien-pandemien/aktuelle-ausbrueche-epidemien/novel-cov/massnahmen-des-bundes.html#accordion1592594518906"
)
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,5,11)))

"""
March 20:
"""
begin = datetime.datetime(2020, 3, 20)
keyword = dict(
    tag=kw.forbid_assemblies_all,
    description=""" The government announced that no lockdown would be implemented,
                    but all events or meetings over 5 people were prohibited.
                    Reopen: Geöffnet/gestattet seit 30. Mai
                    Treffen in der Öffentlichkeit von maximal 30 Personen (auf öffentlichen Plätzen, Spazierwegen oder Parkanlagen) """,
    references="https://www.bag.admin.ch/bag/de/home/krankheiten/ausbrueche-epidemien-pandemien/aktuelle-ausbrueche-epidemien/novel-cov/massnahmen-des-bundes.html#accordion1592594518906"
)
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,5,30)))
