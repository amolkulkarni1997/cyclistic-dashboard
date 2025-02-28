# 🚲 Cyclistic Bike-Share Data Analysis & Dashboard  

## 📌 Project Overview  
This project explores and visualizes **Chicago’s Cyclistic bike-share data** to understand user behavior and patterns.  
The **final product** is an **interactive Streamlit dashboard** that provides key insights into **rider types, peak usage hours, and station popularity**.

### **🔍 Key Objectives:**
- Analyze **ride trends** for casual users vs. members.  
- Identify **busiest hours & stations**.  
- Develop an **interactive dashboard** to visualize insights.  

---

## 📂 Folder Structure  
📁 **`data/`** _(Stores datasets)_  
- `cleaned_cyclistic_data.csv` → Final **processed dataset** used for analysis.  
- `dashboard_data.csv` → Smaller dataset **extracted** for dashboard use.  
- `divvy_trips.csv` & `divvy_stations.csv` → **Raw datasets** before processing.  

📁 **`notebooks/`** _(Data processing in Jupyter)_  
- `Data Analysis Dashboard.ipynb` → **Data cleaning & preprocessing**.  

📁 **`dashboard/`** _(Code for interactive dashboard)_  
- `dashboard.py` → **Streamlit dashboard script** for visualization.  
- `test_map.py` → **Script for map visualization testing**.  

📁 **`requirements.txt`** _(Dependencies & package list)_  
- Includes required **Python libraries** for running this project.

---

## 🛠️ Data Processing Steps (Python-Based)  
✔ **Raw Data (`divvy_trips.csv`, `divvy_stations.csv`)**  
   - Loaded into **Jupyter Notebook** (`Data Analysis Dashboard.ipynb`).  
   - Cleaned missing values & removed duplicates.  
   - Merged station details with trip data.  

✔ **Processed Data (`cleaned_cyclistic_data.csv`)**  
   - Extracted key features (ride duration, peak hours, rider type).  
   - Created new columns for better insights.  

✔ **Dashboard Data (`dashboard_data.csv`)**  
   - Reduced dataset size for optimized performance.  
   - Used for real-time visualization in Streamlit.

---

## 📊 Insights & Key Findings  
🔹 **Casual riders vs. Members** → Casual users prefer weekends, while members use bikes on weekdays.  
🔹 **Peak Ride Hours** → Rush hours (8 AM & 5 PM) show higher bike usage.  
🔹 **Most Popular Start Stations** → Top stations are clustered near business & tourist areas.  
🔹 **Average Ride Duration** → Casual users tend to ride longer compared to members.  

---

## 🚀 Running the Streamlit Dashboard  
### **1️⃣ Clone this repository:**  
```bash
git clone https://github.com/amolkulkarni1997/cyclistic-dashboard.git
cd cyclistic-dashboard
