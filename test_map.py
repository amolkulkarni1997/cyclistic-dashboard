import streamlit as st
import folium
from streamlit_folium import folium_static

st.title("🌍 Test Folium Map with Marker")

# Create a simple map centered on Chicago
m = folium.Map(location=[41.8781, -87.6298], zoom_start=12)

# Add a single test marker
folium.Marker(
    [41.8781, -87.6298],  # Chicago coordinates
    popup="Test Marker - Chicago",
    icon=folium.Icon(color="blue", icon="info-sign"),
).add_to(m)

# Display the map
folium_static(m)