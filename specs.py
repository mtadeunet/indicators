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
    Minutes1 = 60000,
    Minutes5 = 120000,
    Minutes30 = 1800000,
    Hours1 = 3600000,
    Hours4 = 14400000,
    Hours12 = 43200000,
    Days1 = 86400000,
    Days2 = 172800000,
    Week1 = 604800000

