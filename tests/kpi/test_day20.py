import pandas as pd

from src.reports.peer_report import generate_peer_report

df = pd.DataFrame({

    "company": [
        "TCS",
        "Infosys",
        "Wipro",
        "HDFC Bank",
        "ICICI Bank",
        "SBI"
    ],

    "peer_group": [
        "IT",
        "IT",
        "IT",
        "BANK",
        "BANK",
        "BANK"
    ],

    "roe": [
        35,
        28,
        20,
        18,
        15,
        12
    ],

    "revenue_cagr": [
        20,
        16,
        14,
        12,
        11,
        9
    ],

    "debt_to_equity": [
        0.0,
        0.1,
        0.2,
        5.2,
        4.8,
        6.0
    ],

    "quality_score": [
        95,
        88,
        82,
        80,
        75,
        70
    ],

    "peer_rank": [
        1,
        2,
        3,
        1,
        2,
        3
    ]

})

generate_peer_report(df)

print("Day 20 Completed")