# 🚲 Cyclistic Bike-Share Data Analysis & Dashboard

## 📌 Project Overview
This project analyzes **Chicago’s Cyclistic bike-share** data to understand user behavior. The final product is an **interactive Streamlit dashboard** that visualizes key insights.

## 📂 Folder Structure
- `cleaned_cyclistic_data.csv` → Final **processed** dataset used for analysis.
- `dashboard_data.csv` → Smaller dataset **extracted** specifically for dashboard use.
- `divvy_trips.csv` & `divvy_stations.csv` → **Raw datasets** before processing.
- `Data Analysis Dashboard.ipynb` → **Jupyter Notebook** where **all data processing was done**.
- `dashboard.py` → **Streamlit dashboard script** to visualize the data.
- `test_map.py` → **Testing script** for mapping visualization.

## 🛠️ Data Processing Steps (Python-Based)
1. **Raw Data (`divvy_trips.csv` & `divvy_stations.csv`)**
   - Loaded into **Jupyter Notebook** (`Data Analysis Dashboard.ipynb`).
   - Removed duplicates and handled missing values.
   - Merged station details with trip data.
2. **Processed Data (`cleaned_cyclistic_data.csv`)**
   - Merged dataset with relevant features.
   - Additional feature engineering for analysis.
3. **Dashboard Data (`dashboard_data.csv`)**
   - Extracted key metrics from the processed dataset.
   - Saved separately to optimize dashboard performance.

## 🚀 Running the Streamlit Dashboard
1. **Clone this repository**:
   ```bash
   git clone https://github.com/amolkulkarni1997/cyclistic-dashboard.git
   cd cyclistic-dashboard
