from specs import INTERVALS

settings = {
    "client": "binance",
    "ohlcv": {
        "pair": "ETHBTC",
        "interval": INTERVALS.Days1,
        "start_time": 1609459200,
        "end_time": 1612137600,
    },
    "rsi_ema_count": 14,
}