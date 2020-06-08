# ------------------------------------------------------------------------------ #
# @Author:        Sebastian B. Mohr
# @Email:         
# @Created:       2020-06-05 11:25:02
# @Last Modified: 2020-06-08 13:54:49
# ------------------------------------------------------------------------------ #

import importlib

def get_cps(countries=None):
    """
    Function that returns all change points for different countries.
    They are loaded from there corresponding country python files.

    Parameters
    ----------
    countries : array, string, optional
        if none all countries get returned

    Return
    ------
    change_points: dict
        dict housing all changepoints with country names as keys

    """
    # Default argument
    if countries is None:
        countries = get_possible_countries()
        
    # Cast to list
    if not isinstance(countries, list):
        countries = [countries]

    # Check if the countries are in the all possible countires list
    all_possible = get_possible_countries()
    for country in countries:
        assert country in all_possible ,f"Country '{country}' not in possibles: {all_possible}"

    # Get change points
    change_points = dict()
    for country in countries:
        module = importlib.__import__(country)
        change_points[country] = module.cps

    return change_points


from pathlib import Path
def get_possible_countries():
    """
    Returns list of all possible countries
    """
    results = []
    """
    Lists all python files and removes the change_points file.
    """
    for path in Path('./').rglob('*.py'):
        if path == Path('change_points.py'):
            continue
        results.append(path.stem)
    return results