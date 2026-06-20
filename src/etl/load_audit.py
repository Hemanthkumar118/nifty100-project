import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

tables = pd.read_sql(
"""
SELECT name
FROM sqlite_master
WHERE type='table'
""",
conn
)

audit = []

for table in tables["name"]:
    count = pd.read_sql(
        f"SELECT COUNT(*) as rows FROM {table}",
        conn
    )

    audit.append(
        {
            "table_name": table,
            "row_count": count["rows"][0]
        }
    )

audit_df = pd.DataFrame(audit)

audit_df.to_csv(
    "output/load_audit.csv",
    index=False
)

print(audit_df)

conn.close()