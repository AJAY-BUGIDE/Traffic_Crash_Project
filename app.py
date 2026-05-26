import streamlit as st

from src.analysis import top_streets

st.title("Traffic Crash Analytics")

df = top_streets()

st.subheader("Top 10 Dangerous Streets")

st.dataframe(df)

st.write(
    "These streets have highest crash frequency."
)