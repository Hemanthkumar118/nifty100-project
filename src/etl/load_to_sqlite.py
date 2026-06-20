import pandas as pd
import sqlite3
from pathlib import Path

DB_PATH = "db/nifty100.db"
PROCESSED_PATH = Path("data/processed")

conn = sqlite3.connect(DB_PATH)

for file in PROCESSED_PATH.glob("*.csv"):
    table_name = file.stem

    df = pd.read_csv(file)

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {table_name}")

conn.close()

print("All files loaded successfully!")