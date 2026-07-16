from src.screener.engine import filter_engine


def quality_compounder(df):
    config = {
        "roe_min": 15,
        "debt_to_equity_max": 1,
        "revenue_cagr_min": 10
    }
    return filter_engine(df, config)


def value_pick(df):
    config = {
        "debt_to_equity_max": 2
    }
    return filter_engine(df, config)


def growth_accelerator(df):
    config = {
        "revenue_cagr_min": 15
    }
    return filter_engine(df, config)


def dividend_champion(df):
    return df[df["dividend_yield"] >= 2].reset_index(drop=True)


def debt_free_bluechip(df):
    return df[df["debt_to_equity"] == 0].reset_index(drop=True)


def turnaround_watch(df):
    return df[df["revenue_cagr"] > 10].reset_index(drop=True)