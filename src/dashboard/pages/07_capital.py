import streamlit as st
from src.dashboard.utils.db import *

st.title("💰 Market Capitalization")

market = safe_dataframe(get_market_cap())

if market.empty:
    st.warning("No market cap data available.")
    st.stop()

st.dataframe(market.head(20), use_container_width=True)

if "market_cap" in market.columns:
    st.bar_chart(market["market_cap"])