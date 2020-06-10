""" # Measures for the United Kingdom

We look at the different measures as can be seen on the [Wikipedia timeline](...) and ref....
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
[wikpedia](https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_the_United_Kingdom)
"""
measures = []  # Create empty array on which we append later on

"""
March 9:
"""
begin = datetime.datetime(2020, 3, 9)
keyword = dict(
    tag=kw.restrict_travel_italy,
    description=""" The Foreign and Commonwealth Office advises against all but essential travel to Italy. """,
    )
measures.append(Measure(keyword, begin))


"""
March 12:
"""
begin = datetime.datetime(2020, 3, 12)
keyword = dict(
    tag=kw.stay_home_if_cough,
    description=""" The government advises that anyone with a new continuous
                    cough or a fever should self-isolate for seven days.""",
    )
measures.append(Measure(keyword, begin))


"""
March 13:
The Premier League 2019–2020 season is suspended.
"""
begin = datetime.datetime(2020, 3, 13)
keyword = dict(
    tag=kw.cancel_football,
    description=""" The Premier League 2019–2020 season is suspended. """,
    )
measures.append(Measure(keyword, begin))


"""
March 15:
"""
begin = datetime.datetime(2020, 3, 15)
keyword = dict(
    tag="restrict travel to Spain",
    description=""" The Foreign and Commonwealth Office advises against all but
                    essential travel to Spain."""
    )
measures.append(Measure(keyword, begin))


"""
March 16:
"""
begin = datetime.datetime(2020, 3, 16)
keyword = dict(
    tag="social distancing advice",
    description=""" Prime Minister Boris Johnson advises everyone in the UK against
                    "non-essential" travel and contact with others, to curb coronavirus,
                    as well as to work from home if possible and avoid visiting
                    social venues such as pubs, clubs or theatres. Pregnant women,
                    people over the age of 70 and those with certain health conditions
                    are urged to consider the advice "particularly important", and
                    will be asked to self-isolate within days. """
    )
measures.append(Measure(keyword, begin))


"""
March 17:
"""
begin = datetime.datetime(2020, 3, 17)
keyword = dict(
    tag=kw.only_essential_travel,
    description=""" The Foreign and Commonwealth Office advises against all
                    non-essential international travel due to the pandemic and
                    the border restrictions put in place by many countries in response. """
    )
measures.append(Measure(keyword, begin))


"""
March 20:
"""
begin = datetime.datetime(2020, 3, 20)
keyword = dict(
    tag=kw.close_schools,
    description=""" The government announces that all schools in the country
                    will shut from the afternoon of Friday 20 March, except for
                    those looking after the children of key workers and vulnerable children. """
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 20)
keyword = dict(
    tag=kw.close_res_bars,
    description=""" Prime Minister Boris Johnson orders all cafes, pubs and
                    restaurants to close from the evening of 20 March, except
                    for take-away food, to tackle coronavirus. """
    )
measures.append(Measure(keyword, begin))

begin = datetime.datetime(2020, 3, 20)
keyword = dict(
    tag=kw.close_theaters_cinema,
    description=""" All the UK's nightclubs, theatres, cinemas, gyms and leisure
                    centres are told to close "as soon as they reasonably can". """
    )
measures.append(Measure(keyword, begin))


"""
March 23:
"""
begin = datetime.datetime(2020, 3, 23)
keyword = dict(
    tag=kw.forbid_assemblies_all,
    description=""" Groups of more than three people in public are banned and mayors are
                    given powers to clear public spaces. """)
measures.append(Measure(keyword, begin))

keyword = dict(
    tag=kw.close_shops,
    description=""" ‘Contact professions’ such as hairdressers, nail studios,
                    tattoo parlours and physiotherapists are ordered to close. """
    )
end = datetime.datetime(2020, 5, 11)
measures.append(Measure(keyword, begin, end))


"""
March 24:
"""
begin = datetime.datetime(2020, 3, 24)
keyword = dict(
    tag=kw.lockdown,
    description=""" In a televised address, Boris Johnson announces a UK-wide partial
                    lockdown, to contain the spread of the virus. The British public
                    are instructed that they must stay at home, except for certain
                    "very limited purposes" – shopping for basic necessities; for
                    "one form of exercise a day"; for any medical need; and to travel
                    to and from work when "absolutely necessary". However, when
                    these restrictions came into force on 26 March, the statutory
                    instrument omitted any limit on the number of exercise sessions.
                    [123] A number of other restrictions are imposed, with police
                    given powers to enforce the measures, including the use of fines."""
    )
measures.append(Measure(keyword, begin))

# NOTE: There are some region specific, partial easing of lockdowns on different dates
"""
England:
- May 13: Lockdown measures are eased in England, allowing people to spend more
    time outside, meet someone from another household providing it is on a one-to-one
    such as golf. Garden centres are also allowed to open.[372] House moves and
    viewings are now permitted under the changes.
- June 1: Johnson says the government's five tests have been met, and from 1 June
    in England groups of up to six people will be able to meet outdoors in gardens
    and outdoor private spaces.
    Boris Johnson outlines plans to reopen car showrooms and outdoor markets from
    1 June.
    The third amendment to the Coronavirus Restrictions legislation comes into effect,
    again without prior parliamentary scrutiny. Car and caravan showrooms, outdoor
    sports amenities and outdoor non-food markets may reopen. The prohibitions on
    leaving home are replaced by a prohibition on staying overnight away from home,
    with specific exceptions such as for work. Gatherings of people from more than
    one household are limited to six people outdoors and are prohibited entirely
    indoors, with exceptions including education. There are further exemptions for
    elite athletes.
- June 8: Dental practices will be allowed to reopen from 8 June in England.
Wales:
- May 8: Mark Drakeford, the First Minister of Wales, extends the lockdown restrictions
    for a further three weeks but with some minor changes. People are allowed to
    exercise outside more than once a day and councils can plan for the reopening
    of libraries and tips. Some garden centres can also reopen.
- June 1: Mark Drakeford, the First Minister of Wales, announces an easing of the
    lockdown restrictions for Wales from Monday 1 June, that will allow the members
    of two households to meet up outdoors. Non-essential retailers are urged to
    use the next three weeks to "prepare safeguarding".
    Welsh health minister Vaughan Gething announces an easing of lockdown
    rules for those shielding at home in Wales. From 1 June they may meet up outside
    with people from another household, but must maintain social distancing rules
    and must not go into another person's home.
Scotland:
- May 10: Nicola Sturgeon removes the once-a-day outdoors exercise limit in Scotland
    starting from the following day.
- May 29: First Minister of Scotland Nicola Sturgeon announces an easing of lockdown
    measures in Scotland from the following day, when people from two different
    households can meet up outdoors as long as they are groups of eight or less.
    Lockdown measures are eased in Scotland.
Northern Ireland:
- May 19: Northern Ireland further eases its lockdown measures. Groups of up to
    six people who do not share the same household are allowed to meet up outdoors,
    so long as they maintain social distancing. Churches are allowed to reopen for
    private prayer, and the playing of sports such as golf and tennis can resume.
- June 8: The Northern Ireland Executive agrees to further relax lockdown restrictions
    from 8 June, when large retailers, car showrooms and shops in retail parks will
    be allowed to open, and outdoor weddings attended by ten people will be permitted.
    The Northern Ireland Executive agrees to ease the lockdown measures for people
    shielding at home from 8 June, when they will be allowed outdoors with members
    of their household, or to meet one member of another household if they are living
    alone.

Conclusion:
Everyone easing lockdown substantially between May 29 and June 8
"""

"""
May 11:
"""
begin = datetime.datetime(2020, 5, 11)
keyword = dict(
    tag="back to work if home office impossible",
    description=""" A recorded address by Boris Johnson is broadcast at 7pm in which
                    he outlines a "conditional plan" to reopen society, but says
                    it is "not the time simply to end the lockdown this week", and
                    describes the plans as "the first careful steps to modify our
                    measures". Those who cannot work from home, such as construction
                    workers and those in manufacturing, are encouraged to return
                    to work from the following day, but to avoid public transport
                    if possible. """
    )
measures.append(Measure(keyword, begin))

"""
begin = datetime.datetime(2020, 5, 11)
keyword = dict(
    tag="advice: wear masks in England",
    description=""" The UK government advises people in England to wear face
                    coverings in enclosed spaces where social distancing is not
                    possible, such as on public transport and in shops. """
    )
measures.append(Measure(keyword, begin))
"""

"""
May 16:
"""
begin = datetime.datetime(2020, 5, 16)
keyword = dict(
    tag=kw.demonstration_start,
    description=""" Coronavirus protests involving the gathering of people are
                    held at venues around the UK, including Hyde Park in London,
                    and Glasgow Green in Glasgow. """
    )
measures.append(Measure(keyword, begin))


"""
June 6:
"""
begin = datetime.datetime(2020, 6, 6)
keyword = dict(
    tag="begin anti racism demonstrations",
    description=""" Anti-racism demonstrations are held in cities across the UK;
                    attendees are reported to be in the thousands. """
    )
measures.append(Measure(keyword, begin))


"""
June 15:
"""
begin = datetime.datetime(2020, 6, 15)
keyword = dict(
    tag="shop opening",
    description=""" Business Secretary Alok Sharma confirms that all non-essential
                    retailers in England can reopen from Monday 15 June providing
                    they follow safety guidelines. However, pubs, bars, restaurants
                    and hairdressers must wait until 4 July "at the earliest" to
                    reopen.[554] Prime Minister Boris Johnson announces that zoos
                    and safari parks will also reopen on 15 June. """
    )
measures.append(Measure(keyword, begin))
