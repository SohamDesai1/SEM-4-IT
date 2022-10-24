import pandas as pd
import requests as req

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-01-02'
a = req.get(url)    
earthquake_json = a.json()
earthquake_properties = [quake['properties'] for quake in earthquake_json['features']]
earthquake_df = pd.DataFrame(earthquake_properties)

