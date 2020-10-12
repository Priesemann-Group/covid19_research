# ------------------------------------------------------------------------------ #
# @Author:        Sebastian B. Mohr
# @Email:
# @Created:       2020-10-07 14:37:39
# @Last Modified: 2020-10-07 15:05:36
# https://dc-covid.site.ined.fr/en/data/pooled-datafiles/
# ------------------------------------------------------------------------------ #
import pandas as pd

main_file = "./covid_pooled_29_09.csv"

data = pd.read_csv(main_file)

data = data.rename(
    columns={"death_reference_date": "date", "death_reference_date_type": "date_type"}
)

data = data.set_index(["country", "date", "age_group"])

data = data.drop(
    columns=[
        "region",
        "country_no",
        "country_code",
        "excelsource",
        "excelsheet",
        "pop_date",
        "pop_male",
        "pop_female",
        "pop_both",
        "date_type",
    ]
)


for country in data.index.get_level_values(level="country").unique():
    country_data = pd.DataFrame()
    temp_c = data.xs(key=country, level="country")
    for age_group in temp_c.index.get_level_values(level="age_group").unique():
        print(age_group)
        try:
            country_data[age_group] = temp_c.xs(
                key=age_group, level="age_group"
            ).diff()["cum_death_both"]
        except:
            a = "asd"
    country_data.to_csv(country.replace(" ", "") + ".csv", date_format="%d-%m-%Y")
