from src.analytics.valuation import *

print("DAY 26")

print()

print("FCF Yield")
print(calculate_fcf_yield(500, 10000))

print()

print("P/E Flag")
print(pe_flag(40, 20))
print(pe_flag(10, 20))
print(pe_flag(22, 20))

print()

print("P/B Flag")
print(pb_flag(5, 2))
print(pb_flag(1, 2))
print(pb_flag(2.2, 2))