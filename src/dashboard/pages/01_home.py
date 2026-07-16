import streamlit as st
from src.dashboard.utils.db import *

st.title("🏠 Nifty100 Dashboard")

companies = safe_dataframe(get_companies())
market = safe_dataframe(get_market_cap())
sectors = safe_dataframe(get_sectors())

if companies.empty:
    st.warning("No company data available.")
    st.stop()

st.subheader("Dashboard Summary")

c1, c2, c3 = st.columns(3)

c1.metric("Companies", len(companies))

if not market.empty and "market_cap" in market.columns:
    c2.metric("Total Market Cap", f"{market['market_cap'].sum():,.0f}")
else:
    c2.metric("Total Market Cap", "N/A")

c3.metric("Total Sectors", len(sectors))

st.divider()

st.subheader("Companies")
st.dataframe(companies.head(10), use_container_width=True)

st.divider()

st.subheader("Sectors")

if sectors.empty:
    st.info("No sector data available.")
else:
    st.dataframe(sectors, use_container_width=True)