import os


def export_peer_ranking(df):

    os.makedirs("output", exist_ok=True)

    file = "output/peer_comparison.xlsx"

    df.to_excel(file, index=False)

    print("Peer comparison exported:", file)