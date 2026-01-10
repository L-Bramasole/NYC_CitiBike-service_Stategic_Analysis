############### test#######
import os

print(">>> CURRENT FILE:", __file__)
print(">>> BASE_DIR:", os.path.dirname(os.path.abspath(__file__)))
print(">>> DIR CONTENTS:", os.listdir(os.path.dirname(os.path.abspath(__file__))))
################################################ Citi Bikes DASHABOARD #####################################################

import streamlit as st
import pandas as pd 
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plts
from numerize.numerize import numerize
from PIL import Image
import os


########################### Initial settings for the dashboard ##################################################################


st.set_page_config(page_title = 'NewYork Citi Bikes 2022 Strategy Analysis Dashboard', layout='centered')
st.title("NewYork Citi Bikes 2022-Strategy Dashboard")

# Define side bar
st.sidebar.title("Aspect Selector")
page = st.sidebar.selectbox('Select an aspect of the analysis',
  ["Objectives",   "Weather & Time Dynamics",
  "Most popular stations",
   "Top20 Routes with Interactive map", "Recommendations"])

# ---------------------------------------------------------
# Define base directory for all tables & figures
# ---------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TABLE_DIR = os.path.join(BASE_DIR, "Figures_Tables")
FIG_DIR = os.path.join(BASE_DIR, "Figures_Tables")
HTML_DIR = os.path.join(BASE_DIR, "Figures_Tables")


########################## Import data ###########################################################################################
Top20_start_stations = pd.read_csv(os.path.join(TABLE_DIR, "Top20_start_stations.csv"))
top20_trips = pd.read_csv(os.path.join(TABLE_DIR, "top20_trips.csv"))
rides_temp = pd.read_csv(os.path.join(TABLE_DIR, "citybike2022_weather.csv"))
weekday_top20 = pd.read_csv(os.path.join(TABLE_DIR, "weekday_top20_stations.csv"), index_col=0)
weekday_hour = pd.read_csv(os.path.join(TABLE_DIR, "weekday_hour_rides.csv"), index_col=0)

######################################### DEFINE THE PAGES #####################################################################


### Objectives page

if page == "Objectives":
    st.markdown(
        "#### This dashboard aims at providing helpful insights on the expansion "
        "problems Citi Bikes currently faces based on 2022 data analysis"
    )

    st.markdown(
        """
**Current challenge:** Citi Bikes runs into a situation where customers complain  
about bikes not being available at certain times.  

**Analysis Goal:** This analysis aims to look at the potential reasons behind  
this challenge.  

**The dashboard is separated into 4 sections:**
"""
    )

    st.markdown("- Most popular stations in 2022")
    st.markdown("- Weather & Time Dynamics")
    st.markdown("- Top20 Routes with Interactive map")
    st.markdown("- Summary & Recommendations")

    st.markdown(
        "The dropdown menu on the left **'Aspect Selector'** will take you to the different aspects of the analysis."
    )

    Image1 = Image.open(os.path.join(FIG_DIR, "citybike_image.jpg")) # source: https://citibikenyc.com
    st.image(Image1)

    st.markdown(
        "This analysis is part of a training course performed by Dr. L‑Bramasole "
        "https://github.com/L-Bramasole/NYC_CitiBike-service_Stategic_Analysis.git"
    )

## Weather component and bike usage Page ###############################

elif page == 'Weather & Time Dynamics':
    line1 = make_subplots(specs=[[{"secondary_y": True}]])
    line1.add_trace(
    go.Scatter(
        x=rides_temp['date'], 
        y=rides_temp['ride_count'], 
        name='Daily Bike Rides',
        marker={'color': 'teal'}  
    ),
    secondary_y=False
    )
    line1.add_trace(
    go.Scatter(
        x=rides_temp['date'], 
        y=rides_temp['tavg'], 
        name='Daily Temperature',
        marker={'color': 'white'}  
    ),
    secondary_y=True
    )
    line1.update_layout(
    width=900,   
    height=600,    
    title="Bike Rides correlates with Tempratures all over the year",
    yaxis_title="Daily Bike Rides",
    yaxis2_title="Daily Temperature"
    )
    st.plotly_chart(line1, width="stretch")
    st.markdown("Ridership shows a near-perfect positive correlation with temperature. Demand is seasonal, scaling up from Spring, peaking in Summer, and retreating in Winter, making weather the primary predictor of system load.")

    ### Heatmap for rides volume over the week days aroud the clock ##

    heatmap2 = go.Figure(
        data=go.Heatmap(
        z=weekday_hour.values,
        x=weekday_hour.columns,
        y=weekday_hour.index,
        colorscale="PuBuGn",
        showscale=True
    )
    )

    heatmap2.update_layout(
        title="Rides volume over the week days around the clock",
        xaxis_title="Weekday",
        yaxis_title="Hour of the day",
        width=900,
        height=750
    )

    st.plotly_chart(heatmap2, width="stretch")

    st.markdown(
        "**Weekday Utility**: Usage is strictly governed by the 9‑to‑5 workday, with sharp spikes "
        "at 08:00 and 17:00–18:00. These hours represent the highest strain on dock availability "
        "and require maximum fleet deployment."
    )

    st.markdown(
        "**Weekend Leisure**: The pattern shifts to a broad plateau between 10:00 and 17:00, "
        "indicating a move from time‑sensitive commuting to flexible, recreational travel."
    )

    st.markdown(
        "**Maintenance Window**: The universal ridership \"blackout\" between 00:00 and 06:00 "
        "provides a critical daily window for system‑wide rebalancing and repairs with zero user impact."
    )

########## Create Most popular stations page ################
                   
elif page == 'Most popular stations':

    # Bar chart
    bar1 = go.Figure(
        go.Bar(
            x=Top20_start_stations['start_station_name'],
            y=Top20_start_stations['ride_id'],
            marker={
                'color': Top20_start_stations['ride_id'],
                'colorscale': 'Blues'
            }
        )
    )

    bar1.update_layout(
        title='Top 20 most popular bike stations in NewYork 2022',
        xaxis_title='Start stations',
        yaxis_title='Sum of trips',
        width=900,
        height=600
    )

    st.plotly_chart(bar1, width="stretch")
    st.markdown("")

    ### Heatmap for rides volume of the top20 stations over the week days ###
    heatmap1 = go.Figure(
        data=go.Heatmap(
            z=weekday_top20.values,
            x=weekday_top20.columns,
            y=weekday_top20.index,
            colorscale="PuBuGn",
            showscale=True
        )
    )

    heatmap1.update_layout(
        title="Ride Counts by Weekday for Top 20 Start Stations",
        xaxis_title="Weekday",
        yaxis_title="Top20 Station Name",
        width=1000,
        height=750,
        margin=dict(l=200)
    )

    heatmap1.update_yaxes(
        categoryorder="array",
        categoryarray=weekday_top20.index,
        title_standoff=20
    )

    st.plotly_chart(heatmap1, width="stretch")

    st.markdown(
        "Top 20 popular stations by ride volume ranking confirms that the highest trip volumes "
        "are concentrated in high-density commercial and recreational corridors. The leadership "
        "of the **West St & Chambers St, W 21 St & 6 Ave, and Broadway & W 58 St** stations—located "
        "near the Hudson River Greenway and major financial centers—highlights the heavy reliance "
        "on Citi Bike for both scenic commuting and connecting users to the heart of Midtown all "
        "days of the week including weekends!"
    )

    st.markdown(
        "From an operational standpoint, these three stations are the highest priority for dock "
        "maintenance and bicycle replenishment to meet consistent daily demand."
    )

    st.markdown(
        "The heatmap distinguishes the other stations by weekday usage. This distinction should be "
        "considered when allocating bike numbers throughout the week and planning maintenance service."
    )

    
### Interactive map with Top Routs  Page #####################################
elif page == 'Top20 Routes with Interactive map': 

    # Top 20 trips bar chart
    
    bar2 = go.Figure(
    go.Bar(
        x=top20_trips['trip_count'],
        y=top20_trips['route'],
        orientation='h',
        marker=dict(
            color=top20_trips['trip_count'],
            colorscale='viridis'
        )
    )
    )

    bar2.update_layout(
    title='Top 20 Most Frequent Routs',
    xaxis_title='Number of Trips',
    yaxis_title='Route (Start → End)',
    yaxis=dict(tickfont=dict(size=10)),
    margin=dict(l=200),  # give more space for long labels
    width=900,
    height=600
    )
    st.plotly_chart(bar2, width="stretch")
    st.markdown(
        "**Recreational Dominance**: Remarkably, nearly 50% of the top 20 routes are round trips (starting and ending at the same station)."
        "This indicates that a massive portion of Citi Bike’s high-frequency traffic is driven by recreational \"loop\" riding"
        "specifically around Central Park, Roosevelt Island, and the Hudson River—rather than simple point-to-point transit."
    )

    st.markdown(
        "**The Chelsea Corridor Link**: Outside of the loops, the high volume on the W 21st St to 9th Ave route identifies it as a critical crosstown connector."
        "This serves as the primary \"utility\" route for commuters moving between the 6th Avenue subway lines and the Chelsea/High Line commercial hubs."
    )
    st.markdown(
    "**Anchor Hubs**: Stations like Grand Army Plaza and Central Park S act as the system's highest-priority gateways. "
    "They are unique because they support both the city's top recreational loops and its most frequent one-way transit trips."
    )

    # Load interactive pydeck map
    path_to_html = os.path.join(HTML_DIR, "top50_routes_directional.html")

    with open(path_to_html, 'r', encoding='utf-8') as f:
        html_data = f.read()

    st.components.v1.html(html_data, height=600)
    ## Show in webpage
    st.header("Aggregated Top50 Bike Trips in NewYork 2022")
    st.markdown("The arcs represent the \"flow\" of riders between stations, with the thickness or color intensity indicating trip volume."
                "Notably, the map appears to show fewer than 50 distinct arcs; this is due to the high density of round-trip activity and shared transit corridors."
                "Round trips (which account for nearly half of the top routes) manifest as static points rather than visible arcs,"
                "while several high-volume routes overlap along the same geographic paths between Midtown and the Hudson River."
               )

     # Load Unique Trips Distribution png

    Distribution = Image.open(os.path.join(FIG_DIR, "Unique Trips Distribution.png"))
    st.image(Distribution)

    st.markdown("highly skewed (long tail)distribution. 75% of all unique routes occur only once in 2022 Citibike dataset."
                "A small number of routes are used very frequently."
                "This is extremely common in mobility data. Human movement is highly diverse, and most people don’t repeat the exact same start–end station combination."
               )
    st.markdown("This is a classic Pareto pattern: Most routes are rare, but a few routes dominate usage.")

    

else:
    
    st.header("Recommendations")

    Image2 = Image.open("Figures_Tables/citi-bike.jpg")  # source: https://inhabitat.com/citi-bike-share-program-launches-in-new-york-with-6000-bikes/
    st.image(Image2)

    st.markdown("## 🛠 Action Plan: Fleet & Station Optimization")

    st.markdown("### 1. Move Bikes at the Right Times")

    st.markdown("- Weekday mornings: Clear docks in Midtown and the Financial District so commuters can park bikes."
                "- Weekday evenings: Refill docks in residential areas and transit hubs for the ride home."
                "- Weekends: Shift extra bikes to Central Park, the Hudson River, and Roosevelt Island for recreational demand."
                "- Midnight–6 a.m.: Do all heavy rebalancing and repairs when riders aren’t using the system."
                
               )

    st.markdown("### 2. Treat Stations Differently")

    st.markdown("Not all stations work the same, so they shouldn’t be managed the same."
                "- Busy commuter stations (like West & Chambers): Need fast bike turnover and frequent checks."
                "- Recreational loop stations (like Central Park): Need mechanics on-site more than extra bikes, because bikes return to the same place."
                "- Regular neighborhood stations: Adjust bike numbers based on weekday vs. weekend patterns."
               )

    st.markdown("### 3. Fix Data Gaps to Improve Operations")

    st.markdown("- 76% of routes happen only once.This spreads bikes across many low‑use routes, causing shortages at popular stations."
                "→ Use Net Flow (starts minus ends) to track where bikes pile up or disappear."
                "- ~37,000 trips have missing end‑station coordinates. These “lost” trips hide real demand and make rebalancing less accurate."
                "→ Add checks to ensure every trip closes with a valid end station."
                "- Track lost demand. Count “full dock” and “empty dock” events to measure missed revenue."
                "- Include e‑bike battery levels in relocation planning.
                )

    st.markdown("### 💡 Bottom Line")

    st.markdown(
        """
> *“Citi Bike doesn’t need more bikes — it needs bikes in the right place at the right time."
"If you want, I can also turn this into a slide‑ready bullet list or a spoken script."
"> By aligning our logistics with the 08:00/17:00 weekday peaks and the 50% weekend round‑trip trend,  
"> we can maximize revenue without increasing capital costs.”*
"""
    )

