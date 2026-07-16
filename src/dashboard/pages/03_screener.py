import streamlit as st

from dashboard.utils.db import *

st.title("📈 Stock Screener")

df = safe_dataframe(get_ratios())

if df.empty:
    st.warning("No financial ratio data available.")
    st.stop()

st.write(f"Companies : {len(df)}")

st.dataframe(df, use_container_width=True)