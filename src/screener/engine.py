import pandas as pd


def filter_engine(df, config):

    result = df.copy()

    if "roe" in result.columns and "roe_min" in config:
        result = result[result["roe"] >= config["roe_min"]]

    if "debt_to_equity" in result.columns and "debt_to_equity_max" in config:
        result = result[
            result["debt_to_equity"] <= config["debt_to_equity_max"]
        ]

    if "revenue_cagr" in result.columns and "revenue_cagr_min" in config:
        result = result[
            result["revenue_cagr"] >= config["revenue_cagr_min"]
        ]

    return result.reset_index(drop=True)