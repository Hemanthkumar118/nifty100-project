from src.dashboard.utils.db import *

print("=" * 50)
print("DAY 22 DASHBOARD TEST")
print("=" * 50)

companies = get_companies()
print("\nCompanies Table")
print(companies.head())

market = get_market_cap()
print("\nMarket Cap Table")
print(market.head())

peers = get_peer_groups()
print("\nPeer Groups")
print(peers.head())

sectors = get_sectors()
print("\nSectors")
print(sectors.head())

print("\nDay 22 Test Passed Successfully")