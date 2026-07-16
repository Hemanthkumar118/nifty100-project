import pandas as pd

from src.analytics.cashflow_kpis import cashflow_intelligence

sample = pd.DataFrame({

    "company_id":[1,2],

    "sector":["IT","Finance"],

    "cash_from_operations":[120,-50],

    "profit_after_tax":[100,40],

    "cash_from_investing":[-30,-200],

    "cash_from_financing":[-20,150],

    "sales":[1000,1200],

    "free_cash_flow_cr":[80,-15]

})

report, distress = cashflow_intelligence(sample)

print("="*50)
print("DAY 31 CASHFLOW INTELLIGENCE")
print("="*50)

print(report)

print("\nDISTRESS COMPANIES")

print(distress)

report.to_excel(
    "output/cashflow_intelligence.xlsx",
    index=False
)

distress.to_csv(
    "output/distress_alerts.csv",
    index=False
)

print("\nFiles Generated Successfully")