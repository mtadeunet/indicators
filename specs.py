from enum import Enum

OHLCV_SPEC = {
    "id": int,
    "open": float,
    "high": float,
    "low": float,
    "close": float,
    "volume": float,
}


class INTERVALS(Enum):
    Minutes1 = 1,
    Minutes5 = 2,
    Minutes10 = 3,
    Minutes30 = 4,
    Hours1 = 5,
    Hours4 = 6,
    Hours12 = 7,
    Days1 = 8,
    Days2 = 9,
    Week1 = 10
