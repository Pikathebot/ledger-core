from ledger_core.http_client import make_retry_policy


def test_make_retry_policy_returns_retry():
    assert make_retry_policy().total == 3
