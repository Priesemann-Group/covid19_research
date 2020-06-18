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

The keyword attribute of the measure consists of `tags`,`description` and links
to `references`, whereby `description` and `references` are optional.

For more information see file `measure.py`.

## Design choices
We create a file for each country in the data folder!  (e.g. italy.py)
These files hold the governmental measures for each country.
At the end of these files an array with measures `measures` should be created!

There is a getter function (with filters i.e. country, date, keywords) in the separate file `measure.py`.

## Measures
Most frequently used tags can be obtained by importing the keywords module.
```
import keywords as kw
```
This module houses a number of tags in its namespace.

