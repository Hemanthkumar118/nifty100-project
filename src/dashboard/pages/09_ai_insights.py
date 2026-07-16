import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="AI Insights", layout="wide")

st.title("🤖 AI Financial Insights")

st.markdown("---")

# Pros & Cons
if os.path.exists("output/pros_cons_generated.csv"):
    pros = pd.read_csv("output/pros_cons_generated.csv")

    st.subheader("Generated Pros & Cons")
    st.dataframe(pros, use_container_width=True)
else:
    st.warning("Pros & Cons report not found.")

# Distress Alerts
if os.path.exists("output/distress_alerts.csv"):
    distress = pd.read_csv("output/distress_alerts.csv")

    st.subheader("Distress Alerts")
    st.dataframe(distress, use_container_width=True)
else:
    st.warning("Distress Alerts file not found.")

# Parsed NLP Output
if os.path.exists("output/analysis_parsed.csv"):
    parsed = pd.read_csv("output/analysis_parsed.csv")

    st.subheader("Parsed Growth Metrics")
    st.dataframe(parsed, use_container_width=True)
else:
    st.warning("Parsed NLP output not found.")