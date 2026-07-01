from src.analytics.cagr import calculate_cagr

print("DAY 10 CAGR TESTS\n")

tests = [
    (100, 200, 5),
    (100, -50, 5),
    (-100, 100, 5),
    (-100, -50, 5),
    (0, 100, 5),
    (100, 100, 0),
]

for start, end, years in tests:
    result, flag = calculate_cagr(start, end, years)

    print("-" * 40)
    print("Start :", start)
    print("End   :", end)
    print("Years :", years)
    print("CAGR  :", result)
    print("Flag  :", flag)