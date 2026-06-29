"""
Financial Ratio Engine
Sprint 2 - Day 08
"""

def net_profit_margin(net_profit, sales):
    if sales == 0:
        return None
    return round((net_profit / sales) * 100, 2)


def operating_profit_margin(operating_profit, sales):
    if sales == 0:
        return None
    return round((operating_profit / sales) * 100, 2)


def return_on_equity(net_profit, equity_capital, reserves):
    capital = equity_capital + reserves

    if capital <= 0:
        return None

    return round((net_profit / capital) * 100, 2)


def return_on_capital_employed(ebit,
                               equity_capital,
                               reserves,
                               borrowings):

    capital = equity_capital + reserves + borrowings

    if capital <= 0:
        return None

    return round((ebit / capital) * 100, 2)


def return_on_assets(net_profit, total_assets):

    if total_assets == 0:
        return None

    return round((net_profit / total_assets) * 100, 2)