import pandas as pd


def calculate_score(df):

    df = df.copy()

    df["quality_score"] = (
        df["roe"] * 0.35 +
        df["revenue_cagr"] * 0.25 +
        (100 - df["debt_to_equity"] * 10) * 0.20 +
        df["dividend_yield"] * 5 * 0.20
    )

    df["quality_score"] = df["quality_score"].round(2)

    return df.sort_values(
        "quality_score",
        ascending=False
    ).reset_index(drop=True)