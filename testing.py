import requests
import pandas as pd
import plotly.express as px
import folium
import json

MAPBOX_API_KEY = 'pk.eyJ1IjoibW9ua3oxMSIsImEiOiJja3ZjcGpkcmNhemljMnBuemllb294Z20yIn0.LFHcV2_PcE_wc5ttNnMM1g'

url = 'https://donnees.montreal.ca/api/3/action/datastore_search?resource_id=c6f482bf-bf0f-4960-8b2f-9982c211addd'
response = requests.get(url)
d = response.json()



df = pd.DataFrame(d['result']['records'])


def plot_coordinates_on_map(df):
    # Drop rows with missing latitude or longitude values
    long = pd.to_numeric(df['LONGITUDE'], errors="coerce").dropna().mean()
    lat = pd.to_numeric(df['LATITUDE'], errors="coerce").dropna().mean()

    # Create a folium map centered at the mean coordinates
    map_center = [lat, long]
    my_map = folium.Map(location=map_center, zoom_start=12)

    # Add markers for each coordinate in the DataFrame
    for index, row in df.iterrows():
        # Ensure that 'LATITUDE' and 'LONGITUDE' are numeric before using them
        lat_1, lon_1 = pd.to_numeric(row['LATITUDE'], errors='coerce'), pd.to_numeric(row['LONGITUDE'], errors='coerce')
        if not pd.isna(lat_1) and not pd.isna(lon_1):
            folium.Marker([lat_1, lon_1]).add_to(my_map)

    # Save the map to an HTML file
    my_map.save('map.html')


plot_coordinates_on_map(df)

