import re
import pandas as pd


def parse_growth(text):
    """
    Extracts:
    10 Years: 21%
    5 Years: 18.4%
    3 Years: -5%

    Returns:
    period, value
    """

    pattern = r"(\d+)\s*Years?:?\s*([-+]?\d+\.?\d*)%"

    match = re.search(pattern, str(text))

    if match:
        years = int(match.group(1))
        value = float(match.group(2))
        return years, value

    return None, None


def parse_dataframe(df, column):

    output = []

    failed = []

    for i, row in df.iterrows():

        years, value = parse_growth(row[column])

        if years is None:
            failed.append(row)
        else:

            output.append({

                "company_id": row.get("company_id", ""),

                "metric_type": column,

                "period_years": years,

                "value_pct": value

            })

    return pd.DataFrame(output), pd.DataFrame(failed)