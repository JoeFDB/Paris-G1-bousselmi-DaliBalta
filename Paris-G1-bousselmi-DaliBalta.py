#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:37:19 2023

@author: joedalibalta
"""

print("Hello from Joe le Bg")

print("hello my team its Joe")
#!pip install geopandas
#!pip install folium
#!pip install geopandas

import pandas as pd
import numpy as np
import geopandas 
import folium

pd.set_option ('display.max_columns', 10)
pd.set_option ('display.width', 1000)
pd.set_option ('display.max_rows', 200)

df1 = pd.DataFrame({
    'Country': ['France', 'Spain', 'Italy', 'Portugal', 'United Kingdom', 'Austria', 'Ireland', 'Germany', 'Poland','Ukraine','Russia','Switzerland' ],
    'Change': [0.0765, 0.141, -0.0162, 0.0936, -0.02, -0.0213,-0.0137, 0.0355, -0.0161, 0.0242, -0.3117,  -0.0002 ],
})

print(df1)
# Create a data frame from the list of dictionaries with the index starting from 1
#df = pd.DataFrame(results, index=range(1, len(results)+1))

# Print the data frame
#print(df1)

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
#print(world)

merged_df = world.merge(df1, how='left', left_on=['name'], right_on=['Country'] )
#merged_df = world.merge(df1, how="left", left_on=['name'], right_on=['change'])
print(merged_df)

#merged_df = merged_df.iloc[:, 1:]
print(merged_df)

my_map = folium.Map()
folium.Choropleth(
    geo_data=merged_df,
    name='choropleth',
    data=merged_df,
    columns=['Country', 'Change'],
    key_on='feature.properties.name',
    fill_color='OrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='%Change'
    
).add_to(my_map)
my_map.save('60StockIndexesVariationthrough2022.html')
display (my_map)
