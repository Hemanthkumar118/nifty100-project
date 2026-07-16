from src.analytics.radar import generate_radar

metrics = [
    "ROE",
    "ROCE",
    "NPM",
    "D/E",
    "FCF",
    "Revenue CAGR",
    "PAT CAGR",
    "Score"
]

values = [
    20,
    18,
    25,
    1,
    30,
    15,
    22,
    85
]

generate_radar(
    "TCS",
    metrics,
    values
)

print("Day 19 Completed")