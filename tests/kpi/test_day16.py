import pandas as pd

from src.screener.presets import *

df = pd.DataFrame({

    "company": [
        "ABC",
        "XYZ",
        "PQR"
    ],

    "roe": [
        18,
        10,
        22
    ],

    "debt_to_equity": [
        0.8,
        2.5,
        0
    ],

    "revenue_cagr": [
        15,
        8,
        25
    ],

    "dividend_yield": [
        2.5,
        0.5,
        3
    ]
})

print("QUALITY COMPOUNDER")
print(quality_compounder(df))

print("\nVALUE PICK")
print(value_pick(df))

print("\nGROWTH ACCELERATOR")
print(growth_accelerator(df))

print("\nDIVIDEND CHAMPION")
print(dividend_champion(df))

print("\nDEBT FREE BLUECHIP")
print(debt_free_bluechip(df))

print("\nTURNAROUND WATCH")
print(turnaround_watch(df))