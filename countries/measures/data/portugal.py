""" # Measures for Portugal
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
[Wikipedia timeline](https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Portugal#Timeline)
"""
measures = []  # Create empty array on which we append later on


"""
March 13:
"""
begin = datetime.datetime(2020, 3, 13)
keyword = dict(
    tag=kw.forbid_assemblies_1000,
    description=""" The Portuguese government declared the highest level of
                    alert because of COVID-19 and said it would be maintained
                    until 9 April.[10] Portugal entered a Mitigation Phase as
                    Community transmission was detected.""",
    references = "https://www.portugal.gov.pt/pt/gc22/comunicacao/comunicado?i=declaracao-de-situacao-de-alerta-ate-9-de-abril-de-2020",
    )
measures.append(Measure(keyword, begin))

keyword = dict(
    tag="Limited access to museums, restaurants, shops, ...",
    description=""" The Portuguese government declared the highest level of
                    alert because of COVID-19 and said it would be maintained
                    until 9 April.[10] Portugal entered a Mitigation Phase as
                    Community transmission was detected.""",
    references = "https://www.portugal.gov.pt/pt/gc22/comunicacao/comunicado?i=restricoes-no-acesso-e-na-afetacao-dos-espacos-nos-estabelecimentos-comerciais-e-nos-de-restauracao-ou-de-bebidas",
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,5,18)))

keyword = dict(
    tag=kw.close_universities,
    description=""" The Council of Ministers yesterday approved a set of
                    extraordinary and urgent measures to respond to the
                    epidemiological situation of the new coronavirus / Covid-19,
                    which highlights the suspension of all academic and
                    non-academic activities with the presence of students in all
                    institutions Higher Education. (Translated from Portuguese)""",
    references = "https://www.portugal.gov.pt/pt/gc22/comunicacao/comunicado?i=suspensao-de-todas-as-atividades-letivas-e-nao-letivas-com-presenca-de-estudantes-em-todas-as-instituicoes-de-ensino-superior",
    )
measures.append(Measure(keyword, begin))


"""
March 17:
"""
begin = datetime.datetime(2020, 3, 17)
keyword = dict(
    tag=kw.social_distancing,
    description=""" COVID19: Wash hands regularly. Avoid social contact. Prevent
                    virus spreading. Follow recommendations. Info
                    http://covid19.min-saude.pt www.prociv.pt / ANEPC-DGS""",
    references = "https://www.portugal.gov.pt/pt/gc22/comunicacao/comunicado?i=covid-19-aviso-a-populacao-por-sms"
    )
measures.append(Measure(keyword, begin))


"""
March 19:
"""
begin = datetime.datetime(2020, 3, 19)

keyword = dict(
    tag=kw.lockdown,
    description=""" António Costa differentiated limitations on the right to
    travel in three situations: people who are sick or under active
    surveillance, people in risk groups and the rest of the population.
    The rest of the population, which does not belong to any risk group and is
    not sick or under active surveillance, "imposes the general duty of home
    care, and must at all costs avoid traveling outside the home beyond what is
    necessary".
    «We have a vast set of exceptions [which will be spelled out in the decree],
    but which are essentially limited to the need to go out for a professional
    activity, assist family members, accompany minors during short-term outdoor
    recreation, walk pets or other situations defined in the decree ”, he said.
    (Translated from Portuguese) """,
    references = [
        "https://www.portugal.gov.pt/pt/gc22/comunicacao/noticia?i=governo-define-limitacoes-de-deslocacao-e-iniciativa-economica"
        ]
    )
measures.append(Measure(keyword, begin, end=datetime.datetime(2020,5,4)))

keyword = dict(
    tag=kw.case_based_isolation,
    description=""" António Costa differentiated limitations on the right to
    travel in three situations: people who are sick or under active
    surveillance, people in risk groups and the rest of the population.
    The first group "imposes mandatory isolation, whether due to hospitalization
    or home care, and the violation of this rule constitutes a crime of
    disobedience". (Translated from Portuguese) """,
    references = [
        "https://www.portugal.gov.pt/pt/gc22/comunicacao/noticia?i=governo-define-limitacoes-de-deslocacao-e-iniciativa-economica"
        ]
    )
measures.append(Measure(keyword, begin))

keyword = dict(
    tag=kw.avoid_going_out_if_risk_group,
    description=""" António Costa differentiated limitations on the right to
    travel in three situations: people who are sick or under active
    surveillance, people in risk groups and the rest of the population.
    People in risk groups, "particularly over 70 years old or with morbidities"
    (particularly serious illnesses), "are imposed a special duty of protection,
    which means that they should only leave their homes in very exceptional
    circumstances and when strictly necessary, to ensure either the acquisition
    of goods, or to go to the bank, the post office or health centers, small
    hygienic walks, or to walk pet animals ». (Translated from Portuguese) """,
    references = [
        "https://www.portugal.gov.pt/pt/gc22/comunicacao/noticia?i=governo-define-limitacoes-de-deslocacao-e-iniciativa-economica"
        ]
    )
measures.append(Measure(keyword, begin))
