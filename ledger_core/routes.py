"""Ledger summary routes."""

import os
from typing import Any


def get_ledger_summary(ledger_id: str) -> dict[str, Any]:
    return {
        "ledger_id": ledger_id,
        "status": "ok",
        "region": os.environ.get("LEDGER_REGION", "unset"),
    }
