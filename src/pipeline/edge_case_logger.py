import sqlite3
import pandas as pd

DB_PATH = "db/nifty100.db"

conn = sqlite3.connect(DB_PATH)

companies = pd.read_sql("SELECT * FROM companies", conn)

log_file = open("output/ratio_edge_cases.log", "w")

log_file.write("===== Sprint 2 Edge Case Report =====\n\n")

for _, row in companies.iterrows():

    company = row.get("company_name", "Unknown")

    sector = str(row.get("broad_sector", ""))

    source_roe = row.get("roe_percentage", None)

    source_roce = row.get("roce_percentage", None)

    if sector.lower() == "financials":
        log_file.write(
            f"{company} : Financial Sector -> D/E warning suppressed\n"
        )

    if source_roe is None:
        log_file.write(
            f"{company} : Missing ROE in source\n"
        )

    if source_roce is None:
        log_file.write(
            f"{company} : Missing ROCE in source\n"
        )

log_file.close()

conn.close()

print("Edge case log generated successfully.")