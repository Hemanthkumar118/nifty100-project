"""
Sprint 2 - Day 10
CAGR Engine
"""

from math import pow


def calculate_cagr(start_value, end_value, years):

    # Edge Case 1
    if years <= 0:
        return None, "INVALID_YEARS"

    # Edge Case 2
    if start_value == 0:
        return None, "ZERO_BASE"

    # Edge Case 3
    if start_value > 0 and end_value < 0:
        return None, "DECLINE_TO_LOSS"

    # Edge Case 4
    if start_value < 0 and end_value > 0:
        return None, "TURNAROUND"

    # Edge Case 5
    if start_value < 0 and end_value < 0:
        return None, "BOTH_NEGATIVE"

    try:

        cagr = (
            (pow(end_value / start_value, 1 / years) - 1)
            * 100
        )

        return round(cagr, 2), "NORMAL"

    except Exception:

        return None, "ERROR"