import pandas as pd

from src.nlp.pros_cons_generator import generate_pros_cons

sample = pd.DataFrame({

    "company_id":[1,2],

    "return_on_equity_pct":[25,7],

    "debt_to_equity":[0.4,3.5],

    "net_profit_margin_pct":[20,2],

    "operating_profit_margin_pct":[25,3],

    "interest_coverage_ratio":[15,1],

    "free_cash_flow_cr":[120,-40],

    "revenue_cagr_5y":[15,3],

    "pat_cagr_5y":[18,2],

    "eps_cagr_5y":[20,1]

})

output = generate_pros_cons(sample)

print("="*50)
print("DAY 30")
print("="*50)

print(output)

output.to_csv(
    "output/pros_cons_generated.csv",
    index=False
)

print("\nSaved -> output/pros_cons_generated.csv")