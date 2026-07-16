import streamlit as st
import os

st.title("📄 Company TearSheets")

folder = "reports/tearsheets"

if os.path.exists(folder):

    pdfs = sorted([f for f in os.listdir(folder) if f.endswith(".pdf")])

    if pdfs:

        pdf = st.selectbox(
            "Select Company",
            pdfs
        )

        with open(os.path.join(folder, pdf), "rb") as file:

            st.download_button(
                "Download TearSheet",
                file,
                pdf,
                mime="application/pdf"
            )

    else:
        st.warning("No PDF files found.")

else:
    st.warning("TearSheet folder not found.")