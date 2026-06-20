import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

checks = []

tables = pd.read_sql(
"""
SELECT name
FROM sqlite_master
WHERE type='table'
""",
conn
)

for table in tables["name"]:
    count = pd.read_sql(
        f"SELECT COUNT(*) as rows FROM {table}",
        conn
    )

    rows = count["rows"][0]

    status = "PASS" if rows > 0 else "FAIL"

    checks.append(
        {
            "table": table,
            "rows": rows,
            "status": status
        }
    )

validation = pd.DataFrame(checks)

validation.to_csv(
    "output/validation_report.csv",
    index=False
)

print(validation)

conn.close()