""" # Measures for Poland
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
Sources are also found in
[Wikipedia timeline](https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Poland#Timeline)
"""
measures = []  # Create empty array on which we append later on


"""
March 10:
"""
begin = datetime.datetime(2020, 3, 10)
keyword = dict(
    tag=kw.forbid_assemblies_1000,
    description=""" On 10 March, authorities cancelled all mass events, defined as those allowing
                    1000 or more participants in the case of stadiums or other events outside of
                    buildings, and those allowing 500 or more participants in the case of events
                    in buildings.""",
    references = "https://zdrowie.trojmiasto.pl/Odwolano-wszystkie-imprezy-masowe-n143077.html",
    )
measures.append(Measure(keyword, begin))


"""
March 12:
"""
begin = datetime.datetime(2020, 3, 12)
keyword = dict(
    tag=kw.close_schools,
    description=""" All schools in Poland were closed starting on 12 March,
                    with a reopening initially scheduled for 25 March 2020.
                    The closure was extended to 10 April, with schools being required to
                    carry out online classes with their students.
                    On 9 April, Mateusz Morawiecki announced that the closure of
                    educational institutions and international transport would continue to 26 April""",
    references = [
        "https://www.gov.pl/web/edukacja/zawieszenie-zajec-w-szkolach",
        "https://tvn24.pl/polska/szkoly-zamkniete-do-wielkanocy-co-z-egzaminami-i-harmonogramem-roku-szkolnego-4377875"]
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,4,26)))

keyword = dict(
    tag=kw.close_universities,
    description=""" Universities cancelled classes for the same period, as schools, while
                    typically keeping research and administrative staff at work and allowing
                    exceptions for research purposes.
                    On 9 April, Mateusz Morawiecki announced that the closure of
                    educational institutions and international transport would continue to 26 April""",
    references = "https://www.umk.pl/wiadomosci/?id=26646"
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,4,26)))

keyword = dict(
    tag=kw.close_theaters_cinema,
    description=""" Cultural institutions, such as philharmonic orchestras, operas, theatres, museums,
                    and cinemas, had their activities suspended beginning on 12 March 2020.
                    Szumowski stated that the closure of cultural institutions and limits
                    implemented in shops would continue to 19 April""",
    references = "https://zdrowie.trojmiasto.pl/Odwolano-wszystkie-imprezy-masowe-n143077.html",
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,4,19)))


"""
March 15:
"""
begin = datetime.datetime(2020, 3, 15)
keyword = dict(
    tag="border closed",
    description=""" the borders would remain "closed" until 3 May""",
    references = "https://www.gov.pl/web/qatar/polands-borders-closed-from-15-march-due-to-coronavirus"   )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,5,1)))


"""
March 25:
"""
begin = datetime.datetime(2020, 3, 25)
keyword = dict(
    tag=kw.forbid_assemblies_all,
    description=""" Constrained gatherings by default to a maximum of two people (with an exception
                    for families); an exception for religious gatherings, such as mass in the Catholic
                    Church, funerals and marriages in which five participants and the person conducting
                    the ceremony were allowed to gather; and an exception for work places.
                    The restrictions were initially defined for the period from 25 March to 11 April inclusive.""",
    references = [
        "https://web.archive.org/web/20200324231929/https://tvn24.pl/polska/koronawirus-w-polsce-zakaz-wychodzenia-z-domu-bez-konkretnego-powodu-i-nowe-obostrzenia-od-25-marca-4512517",
        "https://wiadomosci.gazeta.pl/wiadomosci/7,173952,25816716,czy-mozna-biegac-i-spacerowac-rzecznik-rzadu-policja-nie-bedzie.html"]
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,4,11)))

begin = datetime.datetime(2020, 3, 25)
keyword = dict(
    tag=kw.only_essential_travel,
    description=""" Non-essential travel was prohibited, with the exception of travelling to work or home,
                    SARS-CoV-2 control related activities, or "necessary everyday activities".
                    Everyday activities qualifying as "necessary" included shopping, buying medicines,
                    visiting doctors, walking dogs, jogging, cycling and walking, provided that no more
                    than two people participate and contact with others was avoided.
                    The restrictions were initially defined for the period from 25 March to 11 April inclusive.""",
    references = [
        "https://web.archive.org/web/20200324231929/https://tvn24.pl/polska/koronawirus-w-polsce-zakaz-wychodzenia-z-domu-bez-konkretnego-powodu-i-nowe-obostrzenia-od-25-marca-4512517",
        "https://wiadomosci.gazeta.pl/wiadomosci/7,173952,25816716,czy-mozna-biegac-i-spacerowac-rzecznik-rzadu-policja-nie-bedzie.html"]
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,4,11)))


"""
April 1:
"""
begin = datetime.datetime(2020, 4, 1)
keyword = dict(
    tag="minors not allowed to leave house",
    description=""" According to the regulation, minors (aged under 18) were prohibited from
                    leaving their homes unaccompanied by a legal guardian.""",
    references = "https://web.archive.org/web/20200402023522/http://prawo.sejm.gov.pl/isap.nsf/download.xsp/WDU20200000566/O/D20200566.pdf"   )
measures.append(Measure(keyword, begin))

keyword = dict(
    tag=kw.close_res_bars,
    description=""" Parks, boulevards and beaches were closed, as well as all hairdressers,
                    beauty parlours and tattoo and piercing salons.""",
    references = "https://web.archive.org/web/20200402023522/http://prawo.sejm.gov.pl/isap.nsf/download.xsp/WDU20200000566/O/D20200566.pdf"   )
measures.append(Measure(keyword, begin))

keyword = dict(
    tag=kw.close_hotels,
    description=""" Hotels were allowed to operate only if they had residents in quarantine, in another
                    form of isolation, on an obligatory work delegation for services such as building
                    construction or medical purposes.""",
    references = "https://web.archive.org/web/20200402023522/http://prawo.sejm.gov.pl/isap.nsf/download.xsp/WDU20200000566/O/D20200566.pdf"   )
measures.append(Measure(keyword, begin))

keyword = dict(
    tag=kw.keep_distance,
    description=""" Individuals walking in public were obliged to be separated by at least two metres,
                    with the exception of guardians of children under 13 and disabled persons.""",
    references = "https://web.archive.org/web/20200402023522/http://prawo.sejm.gov.pl/isap.nsf/download.xsp/WDU20200000566/O/D20200566.pdf"   )
measures.append(Measure(keyword, begin))


"""
April 16:
"""
begin = datetime.datetime(2020,4,16)
keyword = dict(
    tag="wear masks",
    description=""" A new control measure was planned to start from 16 April, making it obligatory
                    to cover one's nose and mouth in public places.""",
    references = "https://www.gov.pl/web/koronawirus/zaslon-usta-i-nos"   )
measures.append(Measure(keyword, begin))