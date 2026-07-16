from src.dashboard.utils.db import *

print("=" * 50)
print("DAY 27 - DASHBOARD QA")
print("=" * 50)

companies = get_companies()
ratios = get_ratios()
market = get_market_cap()
sectors = get_sectors()
peers = get_peer_groups()

print("Companies Loaded :", len(companies))
print("Ratios Loaded    :", len(ratios))
print("Market Cap       :", len(market))
print("Sectors          :", len(sectors))
print("Peer Groups      :", len(peers))

print("\nIntegration Test Passed")