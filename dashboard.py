import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from streamlit_folium import folium_static
from folium.plugins import HeatMap

# Load dataset
df = pd.read_csv("dashboard_data.csv").head(100)  # Limit dataset to 100 rows for performance

# Fix column names in case of inconsistencies
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Check for missing start and end coordinates
if "start_lat" not in df.columns or "start_lng" not in df.columns:
    df["start_lat"] = df["latitude"]
    df["start_lng"] = df["longitude"]
if "end_lat" not in df.columns or "end_lng" not in df.columns:
    df["end_lat"] = df["latitude"]
    df["end_lng"] = df["longitude"]

# Convert categorical columns
df["day_of_week"] = df["day_of_week"].astype(str)

# Streamlit Page Config
st.set_page_config(page_title="Cyclistic Dashboard", layout="wide")

# Sidebar Filters
st.sidebar.header("🔍 Filter Data")

# Dropdown for user type
user_type = st.sidebar.selectbox("Select Type of Bicycle Rider", ["All", "Casual", "Member", "Compare Both"])

# Dropdown for day of the week
day = st.sidebar.multiselect("Select Days of the Week", df["day_of_week"].unique(), default=df["day_of_week"].unique())
df = df[df["day_of_week"].isin(day)]

# Data filtering logic
if user_type == "Casual" or user_type == "Member":
    df = df[df["member_casual"] == user_type.lower()]

st.title("🚲 Cyclistic Bike-Share Dashboard")

# Author Info with Icons
st.markdown(
    """
    **Author:** Amol Vivek Kulkarni  
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/amol-vivek-kulkarni-a3834b114/) 
    [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/amolkulkarni1997)
    """,
    unsafe_allow_html=True
)

# Key Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Rides", f"{len(df):,}")
col2.metric("Average Ride Length (min)", f"{df['ride_length'].mean():.2f}")
col3.metric("Most Active Day", df["day_of_week"].value_counts().idxmax())

# Set font style to Times New Roman
plt.rcParams["font.family"] = "Times New Roman"

# Data Analysis Visualizations
st.subheader("📊 Total Rides by Type of Bicycle Rider")
fig, ax = plt.subplots()
sns.countplot(x="member_casual", data=df, palette={"casual": "blue", "member": "red"}, ax=ax)
ax.set_xlabel("Type of User")
ax.set_ylabel("Total Rides")
ax.grid(True, linestyle='dotted', alpha=0.5)
st.pyplot(fig)

st.subheader("⏳ Peak Ride Hours")
fig, ax = plt.subplots()
df_pivot = df.groupby(["hour_of_day", "member_casual"]).size().unstack(fill_value=0)

if user_type == "All":
    df_all = df.groupby("hour_of_day").size().reset_index(name="ride_count")
    sns.lineplot(data=df_all, x="hour_of_day", y="ride_count", color="black", marker="o", ax=ax)
elif user_type == "Compare Both":
    hours = range(0, 24)
    df_pivot = df_pivot.reindex(hours, fill_value=0)
    df_pivot.plot(kind="line", marker="o", ax=ax, color={"casual": "blue", "member": "red"})
    for line in ax.get_lines():
        line.set_linestyle("-.") if any(line.get_ydata() == 0) else line.set_linestyle("-")
else:
    sns.lineplot(data=df_pivot, dashes=False, markers=True, ax=ax, palette={"casual": "blue", "member": "red"})

ax.set_xlabel("Hour of the Day")
ax.set_ylabel("Total Rides")
ax.legend(title="Type of User")
ax.grid(True, linestyle='dotted', alpha=0.5)
st.pyplot(fig)

st.subheader("📍 Top 10 Most Popular Start Stations")
fig, ax = plt.subplots()
df_top_stations = df[df["station_name"].isin(df["station_name"].value_counts().head(10).index)]
if user_type == "All":
    df_top_stations = df.groupby("station_name").size().reset_index(name="ride_count").nlargest(10, "ride_count")
    sns.barplot(data=df_top_stations, y="station_name", x="ride_count", color="gray", ax=ax)
else:
    df_top_stations = df_top_stations.groupby(["station_name", "member_casual"]).size().reset_index(name="ride_count")
    sns.barplot(data=df_top_stations, y="station_name", x="ride_count", hue="member_casual", palette={"casual": "blue", "member": "red"}, ax=ax)
ax.set_xlabel("Total Rides")
ax.set_ylabel("Start Station Name")
ax.legend(title="Type of User")
ax.grid(True, linestyle='dotted', alpha=0.5)
st.pyplot(fig)

st.subheader("📍 Ride Start Locations")
# Create base map
m = folium.Map(location=[df["latitude"].mean(), df["longitude"].mean()], zoom_start=12)
# Add 100 markers only (reduce processing load)
for _, row in df.iterrows():
    folium.Marker(
        [row["latitude"], row["longitude"]],
        popup=row["station_name"],
        icon=folium.Icon(color="blue", icon="info-sign"),
    ).add_to(m)
# Display map
folium_static(m)

st.subheader("🔥 Ride Density Heatmap")
df_heatmap = df.dropna(subset=["latitude", "longitude"])
m = folium.Map(location=[df_heatmap["latitude"].mean(), df_heatmap["longitude"].mean()], zoom_start=12)
HeatMap(data=df_heatmap[["latitude", "longitude"]], radius=10).add_to(m)
folium_static(m)

st.subheader("🚴 Frequent Ride Routes")
df_routes = df.dropna(subset=["start_lat", "start_lng", "end_lat", "end_lng"])
m = folium.Map(location=[df_routes["start_lat"].mean(), df_routes["start_lng"].mean()], zoom_start=12)
for _, row in df_routes.iterrows():
    folium.PolyLine(
        [(row["start_lat"], row["start_lng"]), (row["end_lat"], row["end_lng"])],
        color="blue", weight=10, opacity=0.9,
    ).add_to(m)
folium_static(m)

st.subheader("🏆 Top 5 Busiest Stations")
df_busiest = df["station_name"].value_counts().head(5).index
df_stations_top = df[df["station_name"].isin(df_busiest)]
m = folium.Map(location=[df_stations_top["latitude"].mean(), df_stations_top["longitude"].mean()], zoom_start=12)
for _, row in df_stations_top.iterrows():
    folium.Marker(
        [row["latitude"], row["longitude"]],
        popup=row["station_name"],
        icon=folium.Icon(color="red", icon="star", prefix="fa", icon_size=(20, 20)),
    ).add_to(m)
folium_static(m)
