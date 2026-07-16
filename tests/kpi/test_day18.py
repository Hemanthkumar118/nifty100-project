import pandas as pd

from src.analytics.peer import calculate_peer_rank
from src.analytics.peer_export import export_peer_ranking


df = pd.DataFrame({

    "company":[
        "TCS",
        "Infosys",
        "Wipro",
        "HDFC",
        "ICICI",
        "SBI"
    ],

    "peer_group":[
        "IT",
        "IT",
        "IT",
        "BANK",
        "BANK",
        "BANK"
    ],

    "roe":[
        35,
        28,
        20,
        18,
        15,
        12
    ]

})

result = calculate_peer_rank(df, "roe")

print(result)

export_peer_ranking(result)

print("\nDay 18 Completed")