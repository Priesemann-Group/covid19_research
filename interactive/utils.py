import pandas as pd
import iso3166
import iso3166
import plotly
import plotly.graph_objs as go
import plotly.offline as offline
from plotly.graph_objs import *
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

def make_map(df,observable,str_title, str_save, value_zmax):
    
    #Formats data for the slider
    data_slider = []
    dates = df.date.unique()
    date_i = pd.to_datetime(dates.min())

    for date in dates:

        #Sets Zmax
        if value_zmax < df[df.date == date][observable].max():
            value_zmax = df[df.date == date][observable].max()

        data_day = df[df.date == date]

        data_day = dict(
            type = 'choropleth',
            locations = data_day['code'],
            z = data_day[observable],
            text = data_day['country'],
            zmax = value_zmax,
            zmin = 0,
            colorscale = 'Reds',
        )
        data_slider.append(data_day)

    #Builds slider
    steps = []
    for i in range(len(data_slider)):

        str_date = (date_i + pd.to_timedelta(i,'day')).strftime("%d/%m")

        step = dict(method='restyle',
                    args=['visible', [False] * len(data_slider)],
                    label = str_date,
                   )
        step['args'][1][i] = True
        steps.append(step)

    sliders = [dict(active=0, pad={"t": 1}, steps=steps)]  

    # Sets up layout and data dict
    layout = dict(
        geo=dict(scope='world',projection={'type': 'natural earth'}),
        sliders=sliders,
        title=go.layout.Title(text=str_title)
    )

    plot_dict = dict(data=data_slider, layout=layout) 

    # Plots it in the notebook. Requires plotly jupyter extensions (node.js). Extra-slow.
    #plotly.offline.iplot(plot_dict)

    #Saves to .html and  opens it
    offline.plot(plot_dict, auto_open=True, filename=str_save, validate=True)


def to_iso3_jhu(country): 
    
    iso3_jhu = {'Bolivia':'BOL', 'Brunei':'BRN', 'Burma':'MMR', 'Congo (Brazzaville)':'COG',
       'Congo (Kinshasa)':'COD', "Cote d'Ivoire":'CIV', 'Iran':'IRN', 'Korea, South':'KOR',
       'Laos':'LAO', 'Moldova':'MDA', 'Russia':'RUS', 'Syria':'SYR', 'Taiwan*':'TWN', 'Tanzania':'TZA',
       'United Kingdom':'GBR', 'Venezuela':'VEN', 'Vietnam':'VNM', 'West Bank and Gaza':'PSE'}
    
    if country in iso3_jhu.keys():
        return iso3_jhu[country]
    else:
        try:
            return iso3166.countries.get(country).alpha3
        except:
            raise ValueError('Invalid country')
            
def from_iso3_jhu(iso3): 
    
    iso3_jhu = {'Bolivia':'BOL', 'Brunei':'BRN', 'Burma':'MMR', 'Congo (Brazzaville)':'COG',
       'Congo (Kinshasa)':'COD', "Cote d'Ivoire":'CIV', 'Iran':'IRN', 'Korea, South':'KOR',
       'Laos':'LAO', 'Moldova':'MDA', 'Russia':'RUS', 'Syria':'SYR', 'Taiwan*':'TWN', 'Tanzania':'TZA',
       'United Kingdom':'GBR', 'Venezuela':'VEN', 'Vietnam':'VNM', 'West Bank and Gaza':'PSE'}
    
    iso3_jhu_inv = {iso3_jhu[k] : k for k in iso3_jhu}
    
    if iso3 in iso3_jhu.keys():
        return iso3_jhu[iso3]
    else:
        try:
            return iso3166.countries.get(iso3).name
        except:
            raise ValueError('Invalid country')
            
def download_jhu(data_type, var_new = True):

    #Downloads data
    if data_type == 'cases':
        url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    elif data_type == 'deaths':
        url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
    elif data_type == 'recovered':
        url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

    #Loads and handles dataframe
    df = pd.read_csv(url, sep=',')
    df = df.drop(columns=['Province/State', 'Lat','Long']).groupby('Country/Region').sum().T
    df.reset_index(inplace=True)
    df.rename(columns={'index':'date',"Country/Region":'country'}, inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df = pd.melt(df, id_vars = 'date').rename(columns={'value':data_type})
    
    #Calculates new daily values
    if var_new:
        str_observable = 'new'
        df[str_observable] = df[data_type].diff()
        df.loc[df['date']==df['date'].min(), str_observable] = 0

    #Drops datasets of non-countries
    df = df.drop(df[df['Country/Region'].isin(['MS Zaandam', 'Diamond Princess'])].index)

    #Adds iso3166 code to df, including non-standard cases
    df['code'] = df['Country/Region'].apply(to_iso3_jhu)

    #Downloads population data and adds to df
    url_pop = 'https://raw.githubusercontent.com/datasets/population/master/data/population.csv' 
    df_pop = pd.read_csv(url_pop)
    df_pop = df_pop[df_pop.Year == 2018][['Country Code','Value']].rename(columns={'Country Code':'code', 'Value':'pop'})
    df = df.merge(df_pop, on='code')
    
    return df