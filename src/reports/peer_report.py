import os
import pandas as pd


def generate_peer_report(df):

    os.makedirs("output", exist_ok=True)

    output_file = "output/peer_comparison_report.xlsx"

    with pd.ExcelWriter(output_file) as writer:

        for group in df["peer_group"].unique():

            peer_df = df[df["peer_group"] == group]

            peer_df.to_excel(
                writer,
                sheet_name=str(group)[:31],
                index=False
            )

    print(f"Peer report exported to: {output_file}")