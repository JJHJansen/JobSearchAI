import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time

from helper import *

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

data = pkl_load("data.pkl", "Data/")
data = data[data["LOC"].notna()].reset_index(drop=True)

geolocator = Nominatim(user_agent="ai_jobsearch_project")
geocode = RateLimiter(geolocator.geocode)

addresses = data['LOC'].values

locations, latitudes, longitudes = [], [], []

counter = 0
for address in addresses:
    location = geocode(address)

    if location:
        locations.append(address)
        latitudes.append(location.latitude)
        longitudes.append(location.longitude)

    print(f"{counter} - {address}")

    time.sleep(1.1)
    counter += 1

df_locations = pd.DataFrame([locations, latitudes, longitudes]).T

df_locations.columns = ["LOC", "LAT","LONG"]

df_locations = df_locations.drop_duplicates().reset_index(drop=True)

location_data = data.merge(df_locations, on = 'LOC')

pkl_dump(location_data, "location_data.pkl","Data/")
