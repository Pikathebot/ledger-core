"""Settlement window membership."""


def in_window(txn_date, start, end) -> bool:
    """True if txn_date falls within [start, end) -- end is exclusive."""
    return start <= txn_date < end
