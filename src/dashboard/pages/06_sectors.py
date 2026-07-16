import streamlit as st

from dashboard.utils.db import *

st.title("🏭 Sector Analysis")

sectors = safe_dataframe(get_sectors())

if sectors.empty:
    st.warning("No sector data available.")
    st.stop()

st.dataframe(sectors, use_container_width=True)