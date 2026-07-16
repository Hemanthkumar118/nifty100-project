
import sqlite3
import pandas as pd
import streamlit as st

DB_PATH = "db/nifty100.db"


@st.cache_data(ttl=600)
def run_query(query):
    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql(query, conn)

    conn.close()

    return df


@st.cache_data(ttl=600)
def get_companies():
    return run_query("SELECT * FROM companies")


@st.cache_data(ttl=600)
def get_financial_ratios():
    return run_query("SELECT * FROM financial_ratios")


@st.cache_data(ttl=600)
def get_market_cap():
    return run_query("SELECT * FROM market_cap")


@st.cache_data(ttl=600)
def get_peer_groups():
    return run_query("SELECT * FROM peer_groups")


@st.cache_data(ttl=600)
def get_sectors():
    return run_query("SELECT * FROM sectors")



@st.cache_data(ttl=600)
def get_companies():
    return run_query("SELECT * FROM companies")


@st.cache_data(ttl=600)
def get_market_cap():
    return run_query("SELECT * FROM market_cap")


@st.cache_data(ttl=600)
def get_sectors():
    return run_query("SELECT * FROM sectors")


@st.cache_data(ttl=600)
def get_ratios():
    return run_query("SELECT * FROM financial_ratios")

@st.cache_data(ttl=600)
def run_query(query):
    try:
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Database Error: {e}")
        return pd.DataFrame()
    
    import pandas as pd

def safe_dataframe(df):
    """
    Returns dataframe if data exists,
    otherwise returns empty dataframe.
    """
    if df is None:
        return pd.DataFrame()

    if len(df) == 0:
        return pd.DataFrame()

    return df

import pandas as pd

def safe_dataframe(df):
    if df is None:
        return pd.DataFrame()

    if len(df) == 0:
        return pd.DataFrame()

    return df

@st.cache_data(ttl=600)
def run_query(query):
    try:
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql(query, conn)
        conn.close()
        return df

    except Exception as e:
        print(f"Database Error: {e}")
        return pd.DataFrame()