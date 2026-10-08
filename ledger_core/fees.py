"""Payout fees."""


def net_after_fee(amount: float, rate: float) -> float:
    """Amount the merchant receives after the processing fee."""
    return round(amount * (1 + rate), 2)
