import pandas as pd


def cashflow_intelligence(df):

    results = []

    distress = []

    for _, row in df.iterrows():

        company = row.get("company_id", "")

        sector = row.get("sector", "")

        cfo = row.get("cash_from_operations", 0) or 0

        pat = row.get("profit_after_tax", 0) or 0

        cfi = row.get("cash_from_investing", 0) or 0

        cff = row.get("cash_from_financing", 0) or 0

        sales = row.get("sales", 1) or 1

        fcf = row.get("free_cash_flow_cr", 0) or 0

        # ---------------- CFO QUALITY ---------------- #

        ratio = cfo / pat if pat != 0 else 0

        if ratio >= 1:
            quality = "High Quality"

        elif ratio >= 0.5:
            quality = "Moderate"

        else:
            quality = "Accrual Risk"

        # ---------------- CAPEX ---------------- #

        capex_pct = abs(cfi) / sales * 100

        if capex_pct < 3:
            capex_label = "Asset Light"

        elif capex_pct < 8:
            capex_label = "Moderate"

        else:
            capex_label = "Capital Intensive"

        # ---------------- DISTRESS ---------------- #

        distress_flag = False

        if cfo < 0 and cff > 0:
            distress_flag = True

        # ---------------- DELEVERAGING ---------------- #

        deleveraging = False

        if cff < 0:
            deleveraging = True

        # ---------------- CAPITAL ALLOCATION ---------------- #

        if fcf > 0:
            allocation = "Healthy"

        elif distress_flag:
            allocation = "Distress"

        else:
            allocation = "Neutral"

        results.append({

            "company_id": company,

            "sector": sector,

            "cfo_quality_score": round(ratio,2),

            "cfo_quality_label": quality,

            "capex_intensity_pct": round(capex_pct,2),

            "capex_label": capex_label,

            "fcf": fcf,

            "distress_flag": distress_flag,

            "deleveraging_flag": deleveraging,

            "capital_allocation_label": allocation

        })

        if distress_flag:

            distress.append({

                "company_id": company,

                "sector": sector,

                "CFO": cfo,

                "CFF": cff,

                "PAT": pat

            })

    return pd.DataFrame(results), pd.DataFrame(distress)