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
    """

    def __init__(
        self, keyword, begin, end=None, additional_dates=None,
    ):

        # ------------------------------------------------------------------------------ #
        # Default parameters
        # ------------------------------------------------------------------------------ #
        assert isinstance(begin, datetime.datetime), f"Please use datetime as begin"
        assert isinstance(keyword, str), f"Keyword has to be string!"
        assert isinstance(
            additional_dates, (tuple, list, datetime.datetime, type(None))
        ), f"TODO"
        assert isinstance(
            end, (datetime.datetime, type(None))
        ), f"Please use datetime as end"

        # ------------------------------------------------------------------------------ #
        # Set attributes
        # ------------------------------------------------------------------------------ #
        self.begin = begin
        self.keyword = keyword
        self.end = end
        self.additional_dates = additional_dates


""" # Example
    How to use the class from above to construct a measure
"""
if __name__ == "__main__":

    keyword = "Lockdown"
    begin = datetime.datetime(2020, 3, 4)
    end = datetime.datetime(2020, 4, 4)  # Optional

    begin2 = datetime.datetime(2020, 5, 4)
    end2 = None  # No 2nd end yet

    additional_dates = [
        [begin2, end2],
    ]  # One can add multiple begin/end tuples/lists here

    # Construct measure
    lockdown = Measure(keyword, begin, end, additional_dates)
