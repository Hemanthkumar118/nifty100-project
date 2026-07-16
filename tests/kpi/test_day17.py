import pandas as pd

from src.screener.scoring import calculate_score
from src.screener.export import export_excel


df = pd.DataFrame({

    "company":[
        "ABC",
        "XYZ",
        "PQR"
    ],

    "roe":[
        18,
        10,
        22
    ],

    "revenue_cagr":[
        15,
        8,
        25
    ],

    "debt_to_equity":[
        0.8,
        2.5,
        0
    ],

    "dividend_yield":[
        2,
        1,
        3
    ]

})

result = calculate_score(df)

print(result)

export_excel(result)

print("\nDay 17 Completed")