from ledger_core.fees import net_after_fee


def test_net_after_fee_deducts_fee():
    assert net_after_fee(100.0, 0.03) == 97.0
