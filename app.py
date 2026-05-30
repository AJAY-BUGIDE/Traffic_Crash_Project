import streamlit as st

st.set_page_config(
    page_title="Traffic Crash Analytics",
    layout="wide"
)

st.title("🚦 Traffic Crash Analytics & Safety Intelligence Platform")
st.markdown("Analyze crash patterns, hotspots, injuries, and contributing causes using SQL and Streamlit.")


from src.analysis import *

option = st.sidebar.selectbox(
    "Select Analysis",
    [
        "1. Dangerous Weather & Crash Types",
        "2. Top Injury Streets",
        "3. Injury Percentage by Crash Type",
        "4. Peak Crash Hour by Month",
        "5. Night Time Crash Causes",
        "6. Lighting vs Injuries",
        "7. Traffic Control Device Injuries",
        "8. Hotspot Locations",
        "9. Streets with Highest Injury Rate",
        "10. Most Common Crash Type by Year",
        "11. Average Crashes by Day",
        "12. High Risk Time Slots",
        "13. Top 3 Causes per Crash Type",
        "14. Year Over Year Growth",
        "15. Hotspot Zones"
    ]
)

if option == "1. Dangerous Weather & Crash Types":
    st.subheader("Top 5 Dangerous Weather & Crash Type Combinations")
    st.dataframe(top_dangerous_weather_crash())

elif option == "2. Top Injury Streets":
    st.subheader("Top 10 Streets with Highest Injuries")
    st.dataframe(top_streets())

elif option == "3. Injury Percentage by Crash Type":
    st.subheader("Injury Percentage by Crash Type")
    st.dataframe(injury_percentage_by_crash())

elif option == "4. Peak Crash Hour by Month":
    st.subheader("Peak Crash Hour for Each Month")
    st.dataframe(peak_crash_hour_month())

elif option == "5. Night Time Crash Causes":
    st.subheader("Top 5 Night Time Crash Causes")
    st.dataframe(night_time_causes())

elif option == "6. Lighting vs Injuries":
    st.subheader("Average Injuries by Lighting Condition")
    st.dataframe(lighting_injuries())

elif option == "7. Traffic Control Device Injuries":
    st.subheader("Traffic Control Device with Highest Injuries")
    st.dataframe(traffic_control_injuries())

elif option == "8. Hotspot Locations":
    st.subheader("Top Crash Hotspot Locations")
    st.dataframe(hotspot_locations())

elif option == "9. Streets with Highest Injury Rate":
    st.subheader("Top Streets by Injury Rate")
    st.dataframe(injury_rate_streets())

elif option == "10. Most Common Crash Type by Year":
    st.subheader("Most Common Crash Type by Year")
    st.dataframe(common_crash_type_year())

elif option == "11. Average Crashes by Day":
    st.subheader("Average Crashes Per Hour by Day")
    st.dataframe(crash_day_average())

elif option == "12. High Risk Time Slots":
    st.subheader("High Risk Time Slots")
    st.dataframe(high_risk_time_slots())

elif option == "13. Top 3 Causes per Crash Type":
    st.subheader("Top 3 Causes for Each Crash Type")
    st.dataframe(top_3_causes())

elif option == "14. Year Over Year Growth":
    st.subheader("Year-over-Year Crash Growth")
    st.dataframe(yoy_growth())

elif option == "15. Hotspot Zones":
    st.subheader("Top 10 Hotspot Zones")
    st.dataframe(hotspot_zones())