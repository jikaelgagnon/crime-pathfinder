
import pandas as pd
import plotly.express as px

px.set_mapbox_access_token('pk.eyJ1IjoibW9ua3oxMSIsImEiOiJja3ZjcGpkcmNhemljMnBuemllb294Z20yIn0.LFHcV2_PcE_wc5ttNnMM1g')

df = pd.read_csv('~/Downloads/actes-criminels.csv')

fig = px.scatter_mapbox(
    df, 
    lat = 'Latitude',
    lon = 'Longitude',
    hover_name = 'CATEGORIE',
    zoom = 10
)

fig.show()




