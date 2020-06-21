""" # Measures for Poland
* May need to insert official source for some links
* Perhaps add end dates for theaters and travel
(Comments updated on June 19)
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
                    educational institutions and international transport would continue to 26 April.
                    From May 18, it will be possible to conduct classes:
                    practical in post-secondary schools,
                    revalidation and upbringing as well as early development support and specialist revalidation.
                    On Monday, May 18, institutions and facilities with accommodation
                    and care and educational activities will also be opened. These
                    are e.g. youth hostels, sports centers or community centers.
                    Primary schools open May 25.""",
    references = [
        "https://www.gov.pl/web/edukacja/zawieszenie-zajec-w-szkolach",
        "https://www.gov.pl/web/koronawirus/dodatkowe-wytyczne-dla-dyrektorow-i-nauczycieli-w-zwiazku-z-umozliwieniem-opieki-uczniom-klas-i-iii-i-organizacja-konsultacji-na-terenie-szkoly",
        "https://www.gov.pl/web/koronawirus/3etap"]
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,5,18)))

keyword = dict(
    tag=kw.close_universities,
    description=""" Universities cancelled classes for the same period, as schools, while
                    typically keeping research and administrative staff at work and allowing
                    exceptions for research purposes.
                    On 9 April, Mateusz Morawiecki announced that the closure of
                    educational institutions and international transport would continue to 26 April
                    Reopen: UNIVERSITIES (from May 25)
                    We also want to restore the opportunity to conduct at universities:
                    didactic classes (for final year students),
                    classes that cannot be implemented remotely.
                    Return to classes also applies to the education of doctoral
                    students and classes organized e.g. in laboratories and a medical
                    simulation center.""",
    references = ["https://www.umk.pl/wiadomosci/?id=26646",
                  "https://www.gov.pl/web/koronawirus/3etap"
                  ]
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,5,25)))

keyword = dict(
    tag=kw.close_theaters_cinema,
    description=""" Cultural institutions, such as philharmonic orchestras, operas, theatres, museums,
                    and cinemas, had their activities suspended beginning on 12 March 2020.""",
    references = "https://zdrowie.trojmiasto.pl/Odwolano-wszystkie-imprezy-masowe-n143077.html",
    )
measures.append(Measure(keyword, begin)) # open air is fine already...


"""
March 15:
"""
begin = datetime.datetime(2020, 3, 15)
keyword = dict(
    tag="border closed",
    description=""" Reopen: On Friday, June 12 at At 9.00 the Polish-Lithuanian border was opened.""",
    references = ["https://www.gov.pl/web/qatar/polands-borders-closed-from-15-march-due-to-coronavirus",
                  "https://www.gov.pl/web/koronawirus/granica-polsko-litewska-juz-otwarta"
                  ]
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,6,12)))


"""
March 25:
"""
begin = datetime.datetime(2020, 3, 25)
keyword = dict(
    tag=kw.forbid_assemblies_all,
    description=""" Constrained gatherings by default to a maximum of two people (with an exception
                    for families); an exception for religious gatherings, such as mass in the Catholic
                    Church, funerals and marriages in which five participants and the person conducting
                    the ceremony were allowed to gather; and an exception for work places.""",
    references = [
        "https://web.archive.org/web/20200324231929/https://tvn24.pl/polska/koronawirus-w-polsce-zakaz-wychodzenia-z-domu-bez-konkretnego-powodu-i-nowe-obostrzenia-od-25-marca-4512517",
        ]
    )
measures.append(Measure(keyword, begin))

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
        ]
    )
measures.append(Measure(keyword, begin)) # Can we say that it ended with ending of other measures?


"""
April 1:
"""
begin = datetime.datetime(2020, 4, 1)
keyword = dict(
    tag="minors not allowed to leave house",
    description=""" According to the regulation, minors (aged under 18) were prohibited from
                    leaving their homes unaccompanied by a legal guardian.
                    Reopen: Important! From May 18, children under the age of 13
                    will be able to leave the house without an adult guardian!""",
    references = ["https://web.archive.org/web/20200402023522/http://prawo.sejm.gov.pl/isap.nsf/download.xsp/WDU20200000566/O/D20200566.pdf",
                  "https://www.gov.pl/web/koronawirus/3etap"
                  ]
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020, 5, 18)))

keyword = dict(
    tag=kw.close_res_bars,
    description=""" Parks, boulevards and beaches were closed, as well as all hairdressers,
                    beauty parlours and tattoo and piercing salons.
                    Reopen: From Monday, May 18, we will be able to use the services
                    of a hairdresser and cosmetician, as well as go to restaurants
                    and cafes. """,
    references = ["https://web.archive.org/web/20200402023522/http://prawo.sejm.gov.pl/isap.nsf/download.xsp/WDU20200000566/O/D20200566.pdf",
                  "https://www.gov.pl/web/koronawirus/3etap"
                  ]
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020, 5, 18)))

keyword = dict(
    tag=kw.close_hotels,
    description=""" Hotels were allowed to operate only if they had residents in quarantine, in another
                    form of isolation, on an obligatory work delegation for services such as building
                    construction or medical purposes.
                    Reopen: Hotels, shopping centers and therapeutic rehabilitation will start on May 4th""",
    references = ["https://web.archive.org/web/20200402023522/http://prawo.sejm.gov.pl/isap.nsf/download.xsp/WDU20200000566/O/D20200566.pdf",
                  "https://www.gov.pl/web/koronawirus/kolejny-etap"
                  ]
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020, 5, 4)))

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


"""
June 19:
"""
begin = datetime.datetime(2020,6,19)
keyword = dict(
    tag="open football stadiums",
    description=""" After a break related to the epidemic caused by COVID-19, PKO
                    Ekstraklasa players as well as I and II leagues are coming back
                    to the pitch this weekend. Resumption of competition is the
                    first step in returning to sport normality. Another - that is,
                    partial opening of stadiums for fans - from 19 June. Football
                    fans will be able to take up to 25 percent. seats in stadiums.
                    Importantly - everything will take place in the appropriate
                    sanitary regime.""",
    references = "https://www.gov.pl/web/koronawirus/premier-od-19-czerwca-czesciowo-otwieramy-stadiony-pilkarskie"   )
measures.append(Measure(keyword, begin))
