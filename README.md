# 🚲 CitiBike NYC 2022 – Data Analysis & Operational Insights 

**A data‑driven exploration of station demand, route patterns, and weather effects to support smarter fleet allocation.**

All tasks were completed using Python 3.14 and Python10.required libraries for streamlit dashbord are listed in requirements.txt.


## 📌 Project Overview  
Citi Bike faces a recurring challenge: **customers frequently encounter empty or full stations**, especially during peak commuting hours. This project analyzes **all CitiBike trips from 2022**, enriched with **NOAA weather data**, to uncover the root causes of these imbalances and provide a foundation for smarter fleet distribution and station planning.

Using more than **20 million trip records**, the analysis reveals how station popularity, route patterns, and environmental factors shape bike‑sharing demand across New York City.

---

## 📂 Data Sources  

### 🚲 CitiBike Trip Data (2022)  
open source data from the Citi Bike database for the year 2022 https://s3.amazonaws.com/tripdata/index.html
- 12 monthly CSV files  
- Includes timestamps, station names, GPS coordinates, rider type, and trip duration  
- Combined into a single cleaned dataset representing all rides in 2022  

### 🌤 NOAA Weather Data (LaGuardia Airport) 
NOAA’s API service https://www.noaa.gov/ 
- Daily average temperature (TAVG)  
- Retrieved via NOAA CDO API  
- Merged with trip data by date  

---

## 🧹 Data Preparation  
### CitiBike Data  
- Loaded and concatenated all monthly files  
- Converted timestamps to datetime, extracted durations and cleaned negative & extreme values.
- Extracted date, month, day of week, and ride duration  
- cleaned missing coordinates values and restored or cleaned station names from coordinates
- Created route identifiers (start–end pairs)

### Weather Data  
- Queried NOAA API for station **GHCND:USW00014732**  
- Cleaned and converted temperature and percepitation units  
- Aggregated to daily and monthly averages 
- Merged with Citibie daily rides 

### Final Data Tables
Data set was devided based on questions, cleaned separatly and aggrigated accordingly.
generated tables can be found under Figure_Tables folder of this repositry.
Note: Due to big size of the original dataset, it is not uploaded into this repositry.

---

## ❓ Key Questions  

### 1. Most Popular Stations  
- Which stations have the highest number of departures?  
- How does station usage vary by day of week?  
- How do weekday vs. weekend patterns differ?

### 2. Monthly Trip Trends + Weather Influence  
- How does ridership change across the year?  
- How strongly does temperature correlate with trip volume?

### 3. Most Popular Routes  
- Which start–end station pairs are used most frequently?  
- What do these routes reveal about commuter flows?

### 4. Station Distribution Across NYC  
- Are stations evenly distributed?  
- Where are the geographic gaps?

### 5. Weather + Daily Ridership  
- How do temperature and precipitation affect daily demand?

---

## 📊 Dashboard Structure  
https://nyccitibike-servicestategicanalysis-k3ljnwx4lcafyy7nnbvemz.streamlit.app

The interactive dashboard is divided into **four sections**, each answering a core operational question:

- **Most popular stations in 2022**  
- **Weather & Time Dynamics**  
- **Top 20 Routes (Interactive Map)**  
- **Summary & Recommendations**

---
# 🚀 Running the Dashboard  

To launch the interactive Streamlit dashboard:

```bash
pip install -r requirements.txt
streamlit run citibike2022_nyc_dashboard.py
```

# ⭐ Results Highlights  

### 🔥 1. Station Demand Is Highly Concentrated  
A small cluster of stations — primarily in **Midtown, Lower Manhattan, and transit‑dense areas** — account for a disproportionately large share of departures.  
These stations show strong **AM/PM commuter peaks**, confirming their role in daily work travel.

### 🌤 2. Weather Strongly Shapes Ridership  
- Ridership rises sharply with temperature, peaking in **June–September**  
- Cold months (Jan–Feb) show the lowest usage  
- Daily analysis confirms a clear **positive correlation** between temperature and trip volume

### 🗺 3. Route Patterns Reveal Commuter Corridors  
The top 20 routes form clear directional flows:  
- **Residential → Business districts (AM)**  
- **Business districts → Residential (PM)**  
Weekend patterns shift toward **leisure loops** around parks and waterfronts.

### 📍 4. Station Distribution Shows Coverage Gaps  
While Manhattan is dense with stations, parts of **Queens, Brooklyn, and the Bronx** show sparse coverage, suggesting opportunities for expansion.

### 📈 5. Extreme Skew in Route Frequency  
75% of unique routes occur **only once**, while a small number of routes repeat thousands of times — a classic long‑tail distribution.  
This highlights the importance of focusing operational planning on **high‑frequency corridors**.

---

