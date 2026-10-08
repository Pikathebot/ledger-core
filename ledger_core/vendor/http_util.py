"""Vendored stand-in for a third-party HTTP retry library (no network needed)."""


class Retry:
    def __init__(self, total: int = 3):
        self.total = total
