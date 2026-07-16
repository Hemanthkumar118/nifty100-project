import pandas as pd


def generate_pros_cons(df):

    results = []

    for _, row in df.iterrows():

        company = row.get("company_id", "")

        # KPIs
        roe = row.get("return_on_equity_pct", 0) or 0
        de = row.get("debt_to_equity", 0) or 0
        npm = row.get("net_profit_margin_pct", 0) or 0
        opm = row.get("operating_profit_margin_pct", 0) or 0
        icr = row.get("interest_coverage_ratio", 0) or 0
        fcf = row.get("free_cash_flow_cr", 0) or 0
        revenue = row.get("revenue_cagr_5y", 0) or 0
        pat = row.get("pat_cagr_5y", 0) or 0
        eps = row.get("eps_cagr_5y", 0) or 0

        # ---------------- PRO RULES ---------------- #

        if roe > 20:
            results.append([company, "PRO", 1,
                            "Excellent ROE above 20%", 95])

        if de == 0:
            results.append([company, "PRO", 2,
                            "Debt Free Company", 96])

        if npm > 15:
            results.append([company, "PRO", 3,
                            "Healthy Net Profit Margin", 90])

        if opm > 20:
            results.append([company, "PRO", 4,
                            "Strong Operating Margin", 88])

        if icr > 10:
            results.append([company, "PRO", 5,
                            "Excellent Interest Coverage", 90])

        if fcf > 0:
            results.append([company, "PRO", 6,
                            "Positive Free Cash Flow", 87])

        if revenue > 10:
            results.append([company, "PRO", 7,
                            "Healthy Revenue CAGR", 89])

        if pat > 15:
            results.append([company, "PRO", 8,
                            "Strong Profit Growth", 91])

        if eps > 15:
            results.append([company, "PRO", 9,
                            "EPS Growing Rapidly", 90])

        if roe > 15 and de < 1:
            results.append([company, "PRO", 10,
                            "Efficient capital structure", 92])

        if npm > 20:
            results.append([company, "PRO", 11,
                            "Very High Profitability", 93])

        if revenue > pat:
            results.append([company, "PRO", 12,
                            "Revenue expanding consistently", 82])

        # ---------------- CON RULES ---------------- #

        if de > 2:
            results.append([company, "CON", 1,
                            "High Debt", 95])

        if roe < 10:
            results.append([company, "CON", 2,
                            "Low ROE", 91])

        if npm < 5:
            results.append([company, "CON", 3,
                            "Weak Net Margin", 88])

        if opm < 5:
            results.append([company, "CON", 4,
                            "Poor Operating Margin", 89])

        if icr < 2:
            results.append([company, "CON", 5,
                            "Weak Interest Coverage", 92])

        if fcf < 0:
            results.append([company, "CON", 6,
                            "Negative Free Cash Flow", 90])

        if revenue < 5:
            results.append([company, "CON", 7,
                            "Slow Revenue Growth", 84])

        if pat < 5:
            results.append([company, "CON", 8,
                            "Weak Profit CAGR", 84])

        if eps < 5:
            results.append([company, "CON", 9,
                            "Weak EPS Growth", 83])

        if de > 1 and roe < 12:
            results.append([company, "CON", 10,
                            "High Debt with Low ROE", 95])

        if npm < 0:
            results.append([company, "CON", 11,
                            "Negative Profit Margin", 97])

        if revenue < pat:
            results.append([company, "CON", 12,
                            "Revenue Growing Slower", 80])

    return pd.DataFrame(
        results,
        columns=[
            "company_id",
            "type",
            "rule_id",
            "text",
            "confidence_pct"
        ]
    )