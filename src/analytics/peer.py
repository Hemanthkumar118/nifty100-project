import pandas as pd


def calculate_peer_rank(df, metric):

    df = df.copy()

    df["percentile_rank"] = (
        df.groupby("peer_group")[metric]
        .rank(method="dense", pct=True) * 100
    ).round(2)

    return df