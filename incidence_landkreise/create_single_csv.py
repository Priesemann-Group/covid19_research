import datetime
import json
import pandas

#CONFIG#
lk_id_to_extract = 8435 #Bodenseekreis
#-------------

data = pd.DataFrame(columns=['weekly_cases', 'inzidenz', 'weekly_cases_A00-A04', 'inzidenz_A00-A04',
       'weekly_cases_A05-A14', 'inzidenz_A05-A14', 'weekly_cases_A15-A34',
       'inzidenz_A15-A34', 'weekly_cases_A35-A59', 'inzidenz_A35-A59',
       'weekly_cases_A60-A79', 'inzidenz_A60-A79', 'weekly_cases_A80+',
       'inzidenz_A80+', 'weekly_cases_unbekannt', 'inzidenz_unbekannt'])


# Iter all dates
pbar = tqdm(
    total=pd.date_range(
        start=datetime.datetime(2020, 10, 1), end=datetime.datetime.now()
    ).size
)
for date in pd.date_range(
    start=datetime.datetime(2020, 9, 7), end=datetime.datetime.now()
):
    # Load json
    try:
        df = pd.read_json(
            f"./data/ts/data_{date.strftime('%Y_%m_%d')}.json", orient="values"
        ).T
    except Exception as e:
        break

    # Filter region
    data.loc[date] = df.loc[lk_id_to_extract]
    pbar.update(1)

data.to_csv(f"./timeseries_{lk_id_to_extract}.csv")