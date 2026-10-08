from ledger_core.settlement import reconcile_settlement


def test_settlement_reconciles_at_eod():
    entries = [{"amount": 100.0}, {"amount": -100.0}]
    assert reconcile_settlement(entries) is True
