from src.analytics.cashflow_kpis import *

print("DAY 11 CASH FLOW KPI TESTS\n")

print("=" * 50)

print("1. Free Cash Flow")
print(free_cash_flow(500, -150))

print()

print("2. CFO Quality Score")
print(cfo_quality_score(1200, 1000))

print()

print("3. CapEx Intensity")
print(capex_intensity(-200, 5000))

print()

print("4. FCF Conversion")
print(fcf_conversion(350, 600))

print()

print("5. Capital Allocation Pattern")
print(capital_allocation_pattern(500, -300, -200))