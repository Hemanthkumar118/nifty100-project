import pandas as pd


def calculate_fcf_yield(fcf, market_cap):
    if market_cap in [0, None]:
        return None
    return round((fcf / market_cap) * 100, 2)


def pe_flag(pe, sector_pe):
    if pe is None or sector_pe is None:
        return "Unknown"

    if pe > sector_pe * 1.5:
        return "Caution"

    elif pe < sector_pe * 0.7:
        return "Discount"

    else:
        return "Fair"


def pb_flag(pb, sector_pb):
    if pb is None or sector_pb is None:
        return "Unknown"

    if pb > sector_pb * 1.5:
        return "Caution"

    elif pb < sector_pb * 0.7:
        return "Discount"

    else:
        return "Fair"