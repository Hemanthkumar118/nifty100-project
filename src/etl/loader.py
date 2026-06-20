import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw")

for file in RAW_PATH.glob("*.xlsx"):
    try:
        df = pd.read_excel(file)

        print("=" * 80)
        print("FILE:", file.name)
        print("ROWS:", df.shape[0])
        print("COLUMNS:", df.shape[1])

    except Exception as e:
        print(file.name, e)