import streamlit as st
from src.dashboard.utils.db import *

st.title("🏢 Company Profile")

companies = safe_dataframe(get_companies())

if companies.empty:
    st.warning("No company data available.")
    st.stop()

company = st.selectbox(
    "Select Company",
    companies["company_name"]
)

details = companies[companies["company_name"] == company]

st.dataframe(details, use_container_width=True)