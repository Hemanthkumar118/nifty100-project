import pandas as pd

from src.analytics.cashflow_kpis import cashflow_intelligence
from src.analytics.capital_allocation import generate_capital_report

sample = pd.DataFrame({

    "company_id":[1,2,3,4],

    "sector":["IT","Bank","FMCG","Auto"],

    "cash_from_operations":[120,-20,150,-50],

    "profit_after_tax":[100,50,120,60],

    "cash_from_investing":[-30,-120,-50,-250],

    "cash_from_financing":[-40,200,-10,180],

    "sales":[1000,1200,1800,1600],

    "free_cash_flow_cr":[50,-10,100,-20]

})

cashflow, distress = cashflow_intelligence(sample)

summary, changes = generate_capital_report(cashflow)

print("="*50)
print("DAY 32")
print("="*50)

print("\nCapital Allocation Summary\n")

print(summary)

print("\nPattern Changes\n")

print(changes)

summary.to_excel(
    "output/capital_allocation_summary.xlsx",
    index=False
)

changes.to_csv(
    "output/pattern_changes.csv",
    index=False
)

print("\nFiles Generated Successfully")