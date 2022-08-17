from enum import IntEnum

OHLCV_SPEC = {
    "id": int,
    "open": float,
    "high": float,
    "low": float,
    "close": float,
    "volume": float,
}


class INTERVALS(IntEnum):
    Minutes1 = 60,
    Minutes5 = 120,
    Minutes30 = 1800,
    Hours1 = 3600,
    Hours4 = 14400,
    Hours12 = 43200,
    Days1 = 86400,
    Days2 = 172800,
    Week1 = 604800

