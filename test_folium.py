# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 00:10:05 2015

@author: Gideon
"""

import folium
map_osm = folium.Map(location=[45.5236, -122.6750],
                     tiles='Mapbox Control Room')
map_osm.create_map(path='index.html')
