# Measures

We choose to look at different measures.
These measures can later be mapped onto change points!

## Data (for each measure)
Each measure must have:
* begin date
* keyword

Optional are
* end date
* more dates (on/off measure)

For more information see file `measure.py`.

## Design choices
We create a file for each country in the data folder!  (i.e. germany.py)
This file holds the data for all the measures a country had (see data for each measure above)
At the end of these files an array with measures `measures` should be created!

There is a getter function (with filters i.e. country, date, keywords) in the separate file `measure.py`.

## Measure keywords
Most frequently used keywords can be obtained by importing the keywords module.
```
import keywords as kw
```
This module houses a number of keywords in its namespace.

# QUESTIONS

What happens if measures were taken on a smaller local scale? (i.e. bundesländer)

