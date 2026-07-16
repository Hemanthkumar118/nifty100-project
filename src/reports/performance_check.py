import sqlite3
import pandas as pd
import time

DB = "db/nifty100.db"

start = time.time()

conn = sqlite3.connect(DB)

companies = pd.read_sql("SELECT * FROM companies", conn)
ratios = pd.read_sql("SELECT * FROM financial_ratios", conn)
market = pd.read_sql("SELECT * FROM market_cap", conn)

conn.close()

end = time.time()

print("=" * 50)
print("PERFORMANCE REPORT")
print("=" * 50)

print("Companies :", len(companies))
print("Ratios    :", len(ratios))
print("Market    :", len(market))
print(f"Load Time : {round(end-start,3)} seconds")