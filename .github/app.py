# Debugging GeoPandas
import geopandas as gpd
print("GeoPandas imported successfully!")  # Debugging: Verify GeoPandas is installed

# Streamlit app
import streamlit as st
import folium
from streamlit_folium import st_folium

# Title and description
st.title("GeoJSON Viewer")
st.write("This is a simple app to visualize GeoJSON files.")

# Load GeoJSON file
geojson_path = "lcz_zones.geojson"
 # Update with the path to your GeoJSON file
try:
    gdf = gpd.read_file(geojson_path)
    st.success("GeoJSON file loaded successfully.")
except Exception as e:
    st.error(f"Error loading GeoJSON: {e}")
    st.stop()

# Display basic information about the GeoJSON
st.subheader("GeoJSON Summary")
st.write(gdf.head())

# Create a map
st.subheader("Map Visualization")
m = folium.Map(location=[gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()], zoom_start=10)

# Add GeoJSON to the map
folium.GeoJson(gdf).add_to(m)

# Display the map in Streamlit
st_folium(m, width=700, height=500)
