# ------------------------------------------------------------------------------ #
# @Author:        Sebastian B. Mohr
# @Email:
# @Created:       2020-10-14 10:18:18
# @Last Modified: 2020-10-14 11:01:06
# ------------------------------------------------------------------------------ #
import urllib.request
import zipfile
import datetime
import pandas as pd
import os


def get_new_files():

    url = "https://osf.io/7tnfh/download"
    path = f"./Data_raw/{datetime.date.today().strftime('%d_%m_%Y')}_Output_5.zip"
    urllib.request.urlretrieve(url, path)
    return load_file(path)


def load_file(path):
    with zipfile.ZipFile(path, "r") as z:
        with z.open("Data/Output_5.csv") as f:
            df = pd.read_csv(f, header=3)

    # Formate into multiindex
    df = df.set_index(["Date", "Country", "Age", "Region"])

    df = df.drop(columns=["Sex", "AgeInt", "Code"])

    return df


def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


if __name__ == "__main__":
    # Download new files
    ensure_dir("./Data/")
    ensure_dir("./Data_raw/")
    df = get_new_files()

    # Iterate over each country
    for country in df.index.get_level_values("Country").unique():
        # Select country
        temp = df.xs(country, level="Country")
        # Create folder
        ensure_dir(f"./Data/{country.replace(' ', '')}/")

        # Iterate over each region
        for region in temp.index.get_level_values("Region").unique():
            # Select Region
            temp_2 = temp.xs(region, level="Region")
            # Create folder
            dire = f"./Data/{country.replace(' ', '')}/{region.replace(' ', '')}/"
            ensure_dir(dire)

            # Iterate over all age groups
            a = pd.DataFrame()
            b = pd.DataFrame()
            c = pd.DataFrame()
            for age in temp_2.index.get_level_values("Age").unique():
                temp_3 = temp_2.xs(age, level="Age")
                a[f"{age}"] = temp_3["Cases"]
                b[f"{age}"] = temp_3["Deaths"]
                c[f"{age}"] = temp_3["Tests"]

            a.to_csv(f"{dire}cases.csv")
            b.to_csv(f"{dire}deaths.csv")
            c.to_csv(f"{dire}tests.csv")
