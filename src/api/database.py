import sqlite3
import pandas as pd

DB = "db/nifty100.db"


def run_query(query):

    conn = sqlite3.connect(DB)

    df = pd.read_sql(query, conn)

    conn.close()

    return df