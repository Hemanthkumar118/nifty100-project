import pandas as pd

data = {
    "Company": ["ABB", "TCS", "INFY"],
    "PE": [22, 35, 18],
    "PB": [4.1, 10.5, 6.2],
    "FCF Yield": [4.2, 3.6, 5.1],
    "Flag": ["Fair", "Caution", "Discount"]
}

df = pd.DataFrame(data)

df.to_excel(
    "output/valuation_summary.xlsx",
    index=False
)

print("valuation_summary.xlsx generated")