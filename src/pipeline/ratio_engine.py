import sqlite3
import pandas as pd

from src.analytics.ratios import *
from src.analytics.cagr import *
from src.analytics.cashflow_kpis import *

DB_PATH = "db/nifty100.db"

conn = sqlite3.connect(DB_PATH)

companies = pd.read_sql("SELECT * FROM companies", conn)

rows = []

for _, row in companies.iterrows():

    company = {}

    company["company_id"] = row.get("company_id", None)

    #################################################
    # Profitability
    #################################################

    company["net_profit_margin_pct"] = net_profit_margin(
        row.get("net_profit", 0),
        row.get("sales", 0)
    )

    company["operating_profit_margin_pct"] = operating_profit_margin(
        row.get("operating_profit", 0),
        row.get("sales", 0)
    )

    company["return_on_equity_pct"] = return_on_equity(
        row.get("net_profit", 0),
        row.get("equity_capital", 0),
        row.get("reserves", 0)
    )

    #################################################
    # Leverage
    #################################################

    company["debt_to_equity"] = debt_to_equity(
        row.get("borrowings", 0),
        row.get("equity_capital", 0),
        row.get("reserves", 0)
    )

    #################################################
    # Asset Turnover
    #################################################

    company["asset_turnover"] = asset_turnover(
        row.get("sales", 0),
        row.get("total_assets", 0)
    )

    #################################################
    # Cash Flow
    #################################################

    company["free_cash_flow_cr"] = free_cash_flow(
        row.get("operating_activity", 0),
        row.get("investing_activity", 0)
    )

    rows.append(company)

financial_ratios = pd.DataFrame(rows)

financial_ratios.to_sql(
    "financial_ratios",
    conn,
    if_exists="replace",
    index=False
)

print(financial_ratios.head())

print()

print("Rows :", len(financial_ratios))

conn.close()