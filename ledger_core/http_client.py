"""Thin wrapper around the vendored retry policy."""

from ledger_core.vendor.http_util import Retry


def make_retry_policy() -> Retry:
    return Retry(total=3)
