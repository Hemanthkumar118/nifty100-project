import streamlit as st
from src.dashboard.utils.db import *

st.title("📉 Financial Trends")

market = safe_dataframe(get_market_cap())

if market.empty:
    st.warning("No trend data available.")
    st.stop()

st.line_chart(market["market_cap"])