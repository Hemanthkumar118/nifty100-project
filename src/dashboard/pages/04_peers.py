import streamlit as st
from src.dashboard.utils.db import *

st.title("👥 Peer Comparison")

peers = safe_dataframe(get_peer_groups())

if peers.empty:
    st.warning("No peer group data available.")
    st.stop()

peer = st.selectbox(
    "Select Peer Group",
    sorted(peers["peer_group_name"].dropna().unique())
)

result = peers[peers["peer_group_name"] == peer]

st.dataframe(result, use_container_width=True)