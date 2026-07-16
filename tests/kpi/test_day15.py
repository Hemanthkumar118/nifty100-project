import pandas as pd

from src.screener.engine import filter_engine


df = pd.DataFrame({

    "company":[
        "ABC",
        "XYZ",
        "PQR"
    ],

    "roe":[18,10,22],

    "debt_to_equity":[0.8,2.5,0.5],

    "revenue_cagr":[15,8,25]

})

config = {

    "roe_min":15,

    "debt_to_equity_max":1,

    "revenue_cagr_min":10

}

result = filter_engine(df, config)

print(result)