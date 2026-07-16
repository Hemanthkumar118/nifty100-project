import streamlit as st

import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.append(ROOT)

st.set_page_config(
    page_title="Nifty100 Analytics",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 Nifty100 Financial Intelligence Platform")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Home",
        "Company Profile",
        "Screener",
        "Peers",
        "Trends",
        "Sectors",
        "Capital Allocation",
        "Reports"
    ]
)

st.write("---")

st.write(f"Current Page : **{page}**")

st.sidebar.markdown("---")
st.sidebar.success("Database Connected")
st.sidebar.info("Sprint 4 - Dashboard")