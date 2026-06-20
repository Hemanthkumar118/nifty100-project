import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw")
PROCESSED_PATH = Path("data/processed")

PROCESSED_PATH.mkdir(exist_ok=True)

for file in RAW_PATH.glob("*.xlsx"):

    df = pd.read_excel(file)

    # First row becomes header
    df.columns = df.iloc[0]

    # Remove header row
    df = df[1:]

    # Clean column names
    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    output_file = PROCESSED_PATH / f"{file.stem}.csv"

    df.to_csv(output_file, index=False)

    print(f"Saved: {output_file}")