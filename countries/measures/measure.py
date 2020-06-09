"""
    Helper Class with example for a measure. Is used for the modeling of different countries.
"""
import datetime


class Measure(object):
    """
    A helper class for a measures, they consist of at least one begin- and a corresponding end date.
    Additionaly keywords must be supplied for easier structuring.

    Parameters
    ----------
    begin:datetime.datetime

    end:datetime.datetime, optional

    additional_dates: tuple, datetime.datetime, optional
        If no end then None in tuple
    keyword: array, string
    """
    def __init__(self,
        keyword,
        begin,
        end = None,
        additional_dates = None,
        ):

        # ------------------------------------------------------------------------------ #
        # Default parameters
        # ------------------------------------------------------------------------------ #
        assert isinstance(begin,datetime.datetime), f"Please use datetime as begin"
        assert isinstance(keyword, str), f"Keyword has to be string!"
        assert isinstance(additional_dates, (tuple, list, datetime.datetime, type(None))), f"TODO"
        assert isinstance(end,(datetime.datetime, type(None))), f"Please use datetime as end"

        self.begin = begin

        self.keyword = keyword

        self.end = end

        self.additional_dates = additional_dates



""" # Example
    How to use the class from above to construct a measure
"""
if __name__ == "__main__":

    keyword = "Lockdown"
    begin = datetime.datetime(2020,3,4)
    end = datetime.datetime(2020,4,4) #Optional

    begin2 = datetime.datetime(2020,5,4)
    end2 = None #No 2nd end yet

    additional_dates = [[begin2,end2],] #One can add multplie begin/end tuples here

    #Construct meassure
    lockdown = Measure(keyword,begin,end,additional_dates)
