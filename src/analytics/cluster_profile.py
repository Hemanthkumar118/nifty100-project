import os
import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore

DB = "db/nifty100.db"

FEATURES = [
    "return_on_equity_pct",
    "debt_to_equity",
    "operating_profit_margin_pct",
    "net_profit_margin_pct",
    "asset_turnover",
    "free_cash_flow_cr",
]


def load_data():

    conn = sqlite3.connect(DB)

    ratios = pd.read_sql(
        "SELECT * FROM financial_ratios",
        conn
    )

    conn.close()

    clusters = pd.read_csv(
        "output/cluster_labels.csv"
    )

    # --------------------------
    # Make company_id same datatype
    # --------------------------

    ratios["company_id"] = (
        ratios["company_id"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    clusters["company_id"] = (
        clusters["company_id"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    df = pd.merge(
        ratios,
        clusters,
        on="company_id",
        how="inner"
    )

    return df


def clean_features(df):

    available = []

    for col in FEATURES:

        if col in df.columns:

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

            if not df[col].isna().all():

                df[col] = df[col].fillna(
                    df[col].median()
                )

                available.append(col)

    return df, available


def create_cluster_profile(df, features):

    profile = (
        df.groupby("cluster_id")[features]
        .mean()
        .round(2)
    )

    os.makedirs("output", exist_ok=True)

    profile.to_csv(
        "output/cluster_profile.csv"
    )

    print("✓ Cluster Profile Saved")


def correlation_heatmap(df, features):

    os.makedirs("reports", exist_ok=True)

    corr = df[features].corr()

    plt.figure(figsize=(8,6))

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm"
    )

    plt.tight_layout()

    plt.savefig(
        "reports/correlation_heatmap.png"
    )

    plt.close()

    print("✓ Correlation Heatmap Saved")


def portfolio_statistics(df, features):

    stats = (
        df[features]
        .describe()
        .T
    )

    stats.to_csv(
        "output/portfolio_stats.csv"
    )

    print("✓ Portfolio Statistics Saved")


def outlier_report(df, features):

    z = df[features].apply(zscore)

    mask = (abs(z) > 3).any(axis=1)

    outliers = df.loc[mask]

    outliers.to_csv(
        "output/outlier_report.csv",
        index=False
    )

    print("✓ Outlier Report Saved")


def main():

    print("=" * 60)
    print("SPRINT 6 - DAY 37")
    print("=" * 60)

    df = load_data()

    print("\nMerged Rows:", len(df))

    df, features = clean_features(df)

    print("\nFeatures Used")

    print(features)

    create_cluster_profile(
        df,
        features
    )

    correlation_heatmap(
        df,
        features
    )

    portfolio_statistics(
        df,
        features
    )

    outlier_report(
        df,
        features
    )

    print("\nDAY 37 COMPLETED SUCCESSFULLY")


if __name__ == "__main__":
    main()