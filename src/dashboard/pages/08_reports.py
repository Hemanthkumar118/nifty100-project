import streamlit as st
from src.dashboard.utils.db import *
import os

st.title("📄 Reports")

files = [
    "output/load_audit.csv",
    "output/validation_report.csv",
    "output/peer_comparison.xlsx",
    "output/valuation_summary.xlsx"
]

available = []

for f in files:
    if os.path.exists(f):
        available.append(f)

if len(available) == 0:
    st.warning("No reports available.")
else:
    st.success(f"{len(available)} report(s) found.")
    st.write(available)