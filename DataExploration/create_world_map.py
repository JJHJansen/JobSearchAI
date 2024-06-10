import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time

from helper import *
import folium

data = pkl_load("location_data.pkl", "Data/")

# Initialize a map centered around an average latitude and longitude
world_map = folium.Map(location=[data['LAT'].mean(), data['LONG'].mean()], zoom_start=2)

# Add markers to the map
for idx, row in data.iterrows():
    if pd.notnull(row['LAT']) and pd.notnull(row['LONG']):
        folium.Marker(
            location=[row['LAT'], row['LONG']],
            popup=f"<strong>{row['NAME']}</strong><br>{row['LOC']}",
            tooltip=row['NAME']
        ).add_to(world_map)

# Save map to HTML file
world_map.save('Outputs/firms_map.html')