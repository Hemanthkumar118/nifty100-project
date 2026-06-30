from src.analytics.ratios import *

print("Testing Day 09 Ratios\n")

print("Debt To Equity")
print(debt_to_equity(500,100,100))

print()

print("Debt To Equity (Debt Free)")
print(debt_to_equity(0,100,100))

print()

print("High Leverage Flag")
print(high_leverage_flag(6,"Technology"))

print()

print("Interest Coverage Ratio")
print(interest_coverage_ratio(300,20,100))

print()

print("ICR Label")
print(icr_label(None))

print()

print("ICR Warning")
print(icr_warning(1.2))

print()

print("Net Debt")
print(net_debt(500,100))

print()

print("Asset Turnover")
print(asset_turnover(1200,600))