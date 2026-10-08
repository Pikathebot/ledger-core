"""Settlement reconciliation for end-of-day ledger close."""


def reconcile_settlement(entries: list[dict], timeout: float = 0.5) -> bool:
    """True if the amounts net to zero (abs(sum) < 1e-6)."""
    total = sum(entry["amount"] for entry in entries)
    return abs(total) < 1e-6
