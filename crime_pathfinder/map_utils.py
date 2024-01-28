import requests
import pandas as pd
import plotly.express as px
MAPBOX_API_KEY = 'pk.eyJ1IjoibW9ua3oxMSIsImEiOiJja3ZjcGpkcmNhemljMnBuemllb294Z20yIn0.LFHcV2_PcE_wc5ttNnMM1g'

categories_fr = ['Introduction','Vol dans / sur véhicule à moteur','Vol de véhicule à moteur','Méfait','Vol qualifié','Infraction entraînant la mort']
categories_en = ['Breaking and entering','Theft from a vehicle/theft of vehicle parts','Vehicle theft','General damages','Theft with violence','Murder']
categories_fr_to_en = dict(zip(categories_fr,categories_en))

times_of_day_fr = ['jour','soir','nuit']
times_of_day_en = ['Day','Evening','Night']
times_of_day_fr_to_en = dict(zip(times_of_day_fr,times_of_day_en))


def get_df(year,limit='100000'):
    url = 'https://donnees.montreal.ca/api/3/action/datastore_search?resource_id=c6f482bf-bf0f-4960-8b2f-9982c211addd'
    params = {'q':f'{year}-', 'limit':limit}
    response = requests.get(url,params=params)
    d = response.json()
    df = pd.DataFrame(d['result']['records'])
    return df

def filter_df(df, categories, times_of_day):
    df = df[df['CATEGORIE'].isin(categories)]
    df = df[df['QUART'].isin(times_of_day)]
    return df

def preprocess_df(df):
    df["LONGITUDE"] = pd.to_numeric(df['LONGITUDE'], errors="coerce")
    df["LATITUDE"] = pd.to_numeric(df['LATITUDE'], errors="coerce")
    df["CATEGORIE"] = df["CATEGORIE"].map(categories_fr_to_en)
    df["QUART"] = df["QUART"].map(times_of_day_fr_to_en)

    return df.dropna()

def get_map(df):
    fig = px.scatter_mapbox(df, lat="LATITUDE", lon="LONGITUDE",  color="CATEGORIE",
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=5, zoom=10)
    return fig

def generate_map(year,categories,times_of_day,limit='100000'):
    px.set_mapbox_access_token(MAPBOX_API_KEY)
    df = get_df(year,limit)
    df = preprocess_df(df)
    df = filter_df(df,categories,times_of_day)
    my_map = get_map(df)
    return my_map