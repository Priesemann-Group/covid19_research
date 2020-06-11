"""
    Helper Class with example for a measure. Is used for the modeling of different countries.
"""
import datetime
import keywords as kw
import numpy as np
import importlib

class Measure(object):
    """
    A helper class for a measures, they consist of at least one begin- and a corresponding end date.
    Additionaly keywords must be supplied for easier structuring.

    Parameters
    ----------
    keyword: string
        One should pass a predefined keyword from the keywords dictionary (see `keywords.py`).
        Otherwise a string which can be used as keyword has to be passed.
    begin:datetime.datetime
        Date on which the measure started officially.
    end:datetime.datetime, optional
        Date on which the measure ended officially.
    additional_dates: tuple, datetime.datetime, optional
        Additional begin and end dates, can be used if the measure was reinstated at a later 
        point in time.
        If one wants no end date one should pass None i.e `[[beg1,end1],[beg2,None]]`
    country:string,
        If none gets set automatically by importer
    """

    def __init__(
        self, keyword, begin, end=None, additional_dates=None,country=None
    ):

        # ------------------------------------------------------------------------------ #
        # Default parameters
        # ------------------------------------------------------------------------------ #
        assert isinstance(
            begin, datetime.datetime
        ), f"Please use datetime type as begin date! Not {type(begin)}"
        assert isinstance(
            keyword, dict
        ), f"Keyword has to be a dict containing tag and description! Not {type(keyword)}"
        assert isinstance(
            additional_dates, (tuple, list, datetime.datetime, type(None))
        ), f"Additional dates have to be in a list or tuple format! Not {type(additional_dates)}"
        assert isinstance(
            end, (datetime.datetime, type(None))
        ), f"Please use datetime type as end date! Not {type(end)}"

        # ------------------------------------------------------------------------------ #
        # Set attributes
        # ------------------------------------------------------------------------------ #
        self.begin = begin
        self.keyword = keyword

        if end is None:
            self.end = datetime.datetime(2030, 1, 1)
        self.additional_dates = additional_dates
        self.country= country

    @property
    def tag(self):
        return self.keyword["tag"]
    

def get_measures(countries=None, tag=None, data_begin=None, data_end=None):
    """
    Function that returns all measure of one or multiple countries, can be filtered by tag.

    Parameters
    ----------
    countries : array, string, optional
        if none all countries get returned
    tag : string
        Tag to be filtered by
    data_begin: datetime.datetime, optional
        Get measures on and after data_begin
    data_end: datetime.datetime, optional
        Get measures on and before data_end

    Return
    ------
    :list
        Measures depending on the filter    
    """

    def load_measures_from_file(country):
        module = importlib.import_module("data."+country)
        measures = module.measures
        for measure in measures:
            measure.country=country
        return measures

    # ------------------------------------------------------------------------------ #
    # Default arguments and preliminary looks input parameters
    # ------------------------------------------------------------------------------ #
    if countries is None:
        countries = get_possible_countries()

    if isinstance(countries, str):  # Cast to list
        countries = [countries]

    if tag is None:
        tag = "ALL"

    # Check if the countries are in the all possible countries list
    all_possible = get_possible_countries()
    for country in countries:
        assert country in all_possible ,f"Country '{country}' not in possibles: {all_possible}"

    assert isinstance(data_begin,(datetime.datetime,type(None))), f"Data_begin has to be datetime not {type(data_begin)}"

    # ------------------------------------------------------------------------------ #
    # Filters
    # ------------------------------------------------------------------------------ #

    # Retrieve measures for filtered countries
    filter_countries = []
    for country in countries:
        filter_countries.append(load_measures_from_file(country))
    filter_countries = [y for x in filter_countries for y in x] # Flatten list

    # Filter by tag
    filter_tags = []
    for measure in filter_countries:
        if tag == "ALL":
            filter_tags = filter_countries
            break
        if tag in measure.tag:
            filter_tags.append(measure)
    
    # Filter by date begin
    filter_date_begin = []
    for measure in filter_tags:
        if data_begin is None:
            filter_date_begin = filter_tags
            break
        if measure.begin >= data_begin:
            filter_date_begin.append(measure)

    # Filter by date en
    filter_date_end = []
    for measure in filter_date_begin:
        if data_end is None:
            filter_date_end = filter_date_begin
            break
        if measure.end >= data_end:
            filter_date_end.append(measure)

    return filter_date_end



from pathlib import Path
def get_possible_countries():
    """
    Lists of all countries in the dataset i.e. data folder

    Returns
    -------
    :list
    """
    results = []
    """
    Lists all python files and removes the change_points file.
    """
    for path in Path('./data/').rglob('*.py'):
        results.append(path.stem)
    return results


""" # Example
    How to use the class from above to construct a measure
"""
if __name__ == "__main__":

    keyword = dict(tag=kw.lockdown,description="test")
    begin = datetime.datetime(2020, 3, 4)
    end = datetime.datetime(2020, 4, 4)  # Optional

    begin2 = datetime.datetime(2020, 5, 4)
    end2 = None  # No 2nd end yet

    additional_dates = [
        [begin2, end2],
    ]  # One can add multiple begin/end tuples/lists here

    # Construct measure
    lockdown = Measure(keyword, begin, end, additional_dates)

