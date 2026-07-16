import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

DB_FILE = "db/nifty100.db"

FEATURES = [
    "return_on_equity_pct",
    "debt_to_equity",
    "operating_profit_margin_pct",
    "net_profit_margin_pct",
    "asset_turnover",
    "free_cash_flow_cr",
]


def load_data():
    """Load financial ratios from SQLite."""

    conn = sqlite3.connect(DB_FILE)

    df = pd.read_sql(
        "SELECT * FROM financial_ratios",
        conn
    )

    conn.close()

    return df


def prepare_features(df):
    """Prepare numeric features."""

    available = [c for c in FEATURES if c in df.columns]

    features = df[available].copy()

    # convert to numeric
    for col in features.columns:
        features[col] = pd.to_numeric(features[col], errors="coerce")

    print("\nUsing Features")
    print(features.columns.tolist())

    return features


def clean_data(df):
    """Clean missing values."""

    # Remove columns that are completely empty
    df = df.dropna(axis=1, how="all")

    print("\nColumns After Removing Empty Columns")
    print(df.columns.tolist())

    if df.empty:
        raise ValueError(
            "No usable numeric columns found in financial_ratios table."
        )

    # Fill remaining missing values with median
    for col in df.columns:

        median = df[col].median()

        if pd.isna(median):
            median = 0

        df[col] = df[col].fillna(median)

    return df


def scale_features(df):
    """Standardize features."""

    scaler = StandardScaler()

    return scaler.fit_transform(df)


def create_elbow_plot(data):
    """Generate elbow plot."""

    inertia = []

    for k in range(2, 11):

        model = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )

        model.fit(data)

        inertia.append(model.inertia_)

    os.makedirs("reports", exist_ok=True)

    plt.figure(figsize=(8, 5))

    plt.plot(range(2, 11), inertia, marker="o")

    plt.xlabel("Clusters")

    plt.ylabel("Inertia")

    plt.title("Elbow Plot")

    plt.grid(True)

    plt.savefig("reports/elbow_plot.png")

    plt.close()

    print("✓ Elbow Plot Saved")


def run_kmeans(data):
    """Run clustering."""

    model = KMeans(
        n_clusters=5,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(data)

    return model, labels


def save_clusters(df, model, scaled, labels):
    """Save output."""

    os.makedirs("output", exist_ok=True)

    output = pd.DataFrame()

    output["company_id"] = df["company_id"]

    output["cluster_id"] = labels

    names = {
        0: "Cluster 0",
        1: "Cluster 1",
        2: "Cluster 2",
        3: "Cluster 3",
        4: "Cluster 4"
    }

    output["cluster_name"] = output["cluster_id"].map(names)

    distances = model.transform(scaled)

    output["distance_from_centroid"] = distances.min(axis=1)

    output.to_csv(
        "output/cluster_labels.csv",
        index=False
    )

    print("✓ Cluster Labels Saved")


def main():

    print("=" * 60)
    print("SPRINT 6 - DAY 36")
    print("=" * 60)

    df = load_data()

    print("\nDatabase Columns")
    print(df.columns.tolist())

    features = prepare_features(df)

    features = clean_data(features)

    print("\nCleaned Feature Shape:", features.shape)

    scaled = scale_features(features)

    create_elbow_plot(scaled)

    model, labels = run_kmeans(scaled)

    save_clusters(
        df,
        model,
        scaled,
        labels
    )

    print("\n✓ output/cluster_labels.csv created")
    print("✓ reports/elbow_plot.png created")
    print("\nDAY 36 COMPLETED")


if __name__ == "__main__":
    main()