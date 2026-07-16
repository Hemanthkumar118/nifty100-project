import pandas as pd


def generate_capital_report(df):

    # Count companies in each allocation pattern
    summary = (
        df.groupby("capital_allocation_label")
        .size()
        .reset_index(name="company_count")
    )

    # Placeholder for year-over-year pattern changes
    pattern_changes = df[df["distress_flag"] == True][
        [
            "company_id",
            "sector",
            "capital_allocation_label",
        ]
    ].copy()

    pattern_changes["change"] = "Moved to Distress"

    return summary, pattern_changes