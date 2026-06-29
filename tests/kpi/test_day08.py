import os
import sys

sys.path.insert(0, os.path.abspath("."))

from src.analytics.ratios import *

print("Testing Day 08 Ratios\n")

print("Net Profit Margin")
print(net_profit_margin(200,1000))

print()

print("Operating Profit Margin")
print(operating_profit_margin(150,1000))

print()

print("ROE")
print(return_on_equity(300,100,200))

print()

print("ROCE")
print(return_on_capital_employed(400,100,200,300))

print()

print("ROA")
print(return_on_assets(250,1250))