""" # Create big icu dict with every country

Since there is no unifying data source for corona icu cases we have to retrieve them 
from different sources for every country. The specific sources can be seen
[here](https://docs.google.com/spreadsheets/d/1cnCfGEHqxvMDI2qFPkR3GEzeCTsNXJh_oHt2bi79xZg/edit#gid=0)
"""
""" ## Imports
"""
import pandas as pd
import numpy as np
import datetime
import requests
import lxml.html as lh
""" ## Helper functions
"""


def create_df(date,y):
    """
    Create a pandas dataframe from an date array and an count array
    """
    df = pd.DataFrame()
    df["date"] = date
    df["cases"] = y
    df = df.set_index("date")
    return df


def get_csv(url,column_date_name,column_icu_name,**read_csv_kwargs):
    df = pd.read_csv(url,**read_csv_kwargs)
    df = df.rename(columns={column_date_name: "date", column_icu_name:"cases"})
    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index("date")
    return df

""" ## Countries
"""
def get_all_icu_cases():
    icu = dict() # Dict which will hold our dataframes
    """ ### Austria
    
    Only percent values
    """
    csv_source = "https://info.gesundheitsministerium.at/data/IBAuslastung.csv"
    date_name = r"time"
    icu_name = r"Belegung Intensivbetten in %"
    df = pd.read_csv(csv_source,sep=";")
    df = df.rename(columns={date_name: "date", icu_name:"cases"})
    date_format = "%d.%m.%Y"
    df["date"] = pd.to_datetime(df["date"],format=date_format)
    df = df.set_index("date")
    icu["Austria"] = df

    """ ### Belgium
    """
    temp = pd.read_csv("https://epistat.sciensano.be/Data/COVID19BE_HOSP.csv")
    temp["DATE"] = pd.to_datetime(temp["DATE"])
    temp = temp.rename(columns={"DATE": "date"})
    temp = temp.set_index("date") 
    in_icu = [(date, temp.loc[date].TOTAL_IN_ICU.sum()) for date in pd.date_range(temp.index[0],temp.index[-1])]
    in_icu = np.array(in_icu)
    icu["Belgium"] = create_df(in_icu[:,0],in_icu[:,1])


    """ ### Greece
    """
    url_start = "https://raw.githubusercontent.com/kargig/covid19-gr-json/master/covid-19-gr-"
    url_end = ".json"

    #We iterrate over all files in the repository and extract the json formated files for each date 
    #(if it exists)
    begin = datetime.datetime(2020,3,20)
    end = datetime.datetime.today()

    icu_cases = []
    dates = []
    for date in pd.date_range(begin,end):
        datestr = date.strftime("%Y-%m-%d")
        url = url_start+datestr+url_end
        try:
            data = requests.get(url).json()
            data_exists = True
        except:
            data_exists = False

        if data_exists:
            #Check data type of in icu
            #print(f"Hi {datestr} : {type(data['in_IC'])} : {data['in_IC']}")
            dates.append(date)
            icu_cases.append(data['in_IC'])

    icu["Greece"] = create_df(dates, icu_cases)

    """ ### Italy
    """
    csv_source = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv"
    date_name = "data"
    icu_name = "terapia_intensiva"
    icu["Italy"] = get_csv(csv_source, date_name, icu_name)

    """ ### Netherlands
    """

    csv_source = "https://opendata.arcgis.com/datasets/c121a3cd3ca34e7b8050513307d41b93_0.csv"
    date_name = "date"
    icu_name = "icCount"
    icu["Netherlands"] = get_csv(csv_source, date_name, icu_name)

    """ ## Portugal 

    Gets scraped from daily pdf report and imported to wikipedia.
    We scrape it from wikipedia
    """

    url = "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data/Portugal_medical_cases"
    #Create a handle, page, to handle the contents of the website
    page = requests.get(url)
    #Store the contents of the website under doc
    doc = lh.fromstring(page.content)
    #Parse data that are stored between <tr>..</tr> of HTML
    tr_elements = doc.xpath('//tr')

    #Check the length of rows
    #print([len(T) for T in tr_elements[12:]])
    #Remove rows that are not relevant data
    tr_elements = tr_elements[2:-7]

    #Columns of interest
    date_column = 0
    ICU_column = 12
    column_indices = [date_column, ICU_column]

    #Prepare dfs
    relevant_data = [("date", []), ("cases", [])]

    #Get relevant data out of all data
    for j in range(len(tr_elements)):
        #T is our j'th row
        T = tr_elements[j]
        #i is the index of relevant_data
        i = 0
        #Iterate through each relevant element of the row
        for index in column_indices:
            t = T[index]
            data=t.text_content() 
            #Convert date to usable string
            if index == date_column:
                data = str(data)
                data = data[:-1]
            #Convert ICU cases to integers
            elif index == ICU_column:
                data = int(data)
            #Append the data to the data list of the i'th column
            relevant_data[i][1].append(data)
            #Increment i for the next entry of relevant_data
            i += 1

    #Convert to dataframe
    Dict = {title:column for (title,column) in relevant_data}
    df=pd.DataFrame(Dict)
    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index("date")
    icu["Portugal"] = df

    """ ### Spain
    """
    temp = pd.read_csv('https://covid19.isciii.es/resources/serie_historica_acumulados.csv', encoding='unicode_escape', skipfooter=9, engine='python')
    temp["FECHA"] = pd.to_datetime(temp["FECHA"], format="%d/%m/%Y")
    temp = temp.rename(columns={"FECHA": "date"})
    temp = temp.set_index("date")
    #Sum up ICU cases of the different municipalities to one number per date
    cumulative_in_icu = [(date, temp.loc[date].UCI.sum()) for date in pd.date_range(temp.index[0],temp.index[-1])]

    #Convert from cumulative ICU cases to daily, new ICU cases
    in_icu = [cumulative_in_icu[0]]
    for i in range(len(cumulative_in_icu)-1):
        former_entry = cumulative_in_icu[i]
        new_entry = cumulative_in_icu[i+1]
        new_cases = new_entry[1] - former_entry[1]
        in_icu.append((new_entry[0], new_cases))
        
    in_icu = np.array(in_icu)
    icu["Spain"] = create_df(in_icu[:,0],in_icu[:,1])

    """ ### Slovenia
    """
    url = "https://www.gov.si/assets/vlada/Koronavirus-podatki/COVID-19-vsi-podatki.xlsx"
    temp = pd.read_excel(url)
    temp["Datum"] = pd.to_datetime(temp["Datum"])
    temp = temp.rename(columns={"Datum": "date", "Skupno število hospitaliziranih oseb na posamezni dan": "icu"})
    icu["Slovenia"] = create_df(temp.date, temp.icu)

    """ ### Sweden
    """
    url = "https://www.arcgis.com/sharing/rest/content/items/b5e7488e117749c19881cce45db13f7e/data"
    temp = pd.read_excel(url, sheet_name = 2)
    temp = temp.rename(columns={"Datum_vårdstart": "date", "Antal_intensivvårdade": "icu"})
    temp["date"] = pd.to_datetime(temp["date"])
    icu["Sweden"] = create_df(temp.date, temp.icu)

    """ ### Switzerland
    """
    url = "https://www4.ti.ch/fileadmin/DSS/DSP/UMC/malattie_infettive/Coronavirus/dati/COVID19_Dati_TI_per_github.xlsx"
    temp = pd.read_excel(url)
    temp["date"] = pd.to_datetime(temp["date"])
    icu["Switzerland"] = create_df(temp.date, temp.current_icu)

    return icu

