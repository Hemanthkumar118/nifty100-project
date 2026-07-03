"""
Sprint 2 - Day 11
Cash Flow KPI Engine
"""


def free_cash_flow(operating_activity, investing_activity):
    """
    FCF = Operating Cash Flow + Investing Cash Flow
    Investing activity is usually negative.
    """
    return round(operating_activity + investing_activity, 2)


def cfo_quality_score(cfo, pat):
    """
    CFO / PAT
    """

    if pat == 0:
        return None, "PAT_ZERO"

    score = cfo / pat

    if score > 1:
        label = "High Quality"
    elif score >= 0.5:
        label = "Moderate"
    else:
        label = "Accrual Risk"

    return round(score, 2), label


def capex_intensity(investing_activity, sales):
    """
    CapEx / Sales
    """

    if sales == 0:
        return None, "SALES_ZERO"

    intensity = abs(investing_activity) / sales * 100

    if intensity < 3:
        label = "Asset Light"
    elif intensity <= 8:
        label = "Moderate"
    else:
        label = "Capital Intensive"

    return round(intensity, 2), label


def fcf_conversion(fcf, operating_profit):
    """
    FCF / Operating Profit
    """

    if operating_profit == 0:
        return None

    return round((fcf / operating_profit) * 100, 2)


def capital_allocation_pattern(cfo, cfi, cff):
    """
    Determine company capital allocation pattern.
    """

    cfo_sign = "+" if cfo >= 0 else "-"
    cfi_sign = "+" if cfi >= 0 else "-"
    cff_sign = "+" if cff >= 0 else "-"

    pattern = cfo_sign + cfi_sign + cff_sign

    mapping = {
        "+--": "Reinvestor",
        "++-": "Liquidating Assets",
        "-++": "Distress Signal",
        "--+": "Growth Funded by Debt",
        "+++": "Cash Accumulator",
        "---": "Pre-Revenue",
        "+-+": "Mixed",
    }

    return pattern, mapping.get(pattern, "Unknown")