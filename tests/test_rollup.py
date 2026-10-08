from datetime import date

from ledger_core.rollup import in_window


def test_reconcile_window_boundary():
    start = date(2026, 9, 1)
    end = date(2026, 9, 8)
    assert in_window(date(2026, 9, 1), start, end) is True
    assert in_window(date(2026, 9, 7), start, end) is True
    assert in_window(date(2026, 9, 8), start, end) is False
