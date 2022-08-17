from pybit import HTTP
from specs import INTERVALS, OHLCV_SPEC


BYBIT_KLINE_SPEC = {
    "symbol": str,
    "interval": int,
    "open_time": int,
    "open": float,
    "high": float,
    "low": float,
    "close": float,
    "volume": float,
    "turnover": float
}


class ByBit:
    def __init__(self, settings):
        self._client = HTTP(endpoint="https://api-testnet.bybit.com")

    def convert_interval(self, interval: INTERVALS):
        convertion = {
            "Minutes1": 1,
            "Minutes5": 5,
            "Minutes30": 30,
            "Hours1": 60,
            "Hours4": 240,
            "Hours12": 720,
            "Days1": "D",
            "Week1": "W",
            "Month1": "M"
        }

        return convertion[interval.name]

    def ohlcv(self, pair: str, interval: INTERVALS, **kwargs):
        """Get OHLCV values
        Args:
            symbol (str): the trading pair
            interval (INTERVALS): the interval of kline, e.g 1m, 5m, 1h, 1d, etc.
        Keyword Args:
            limit (int, optional): limit the results. Default 500; max 1000.
            start_time (int, optional): Timestamp in ms to get aggregate trades from INCLUSIVE.
            end_time (int, optional): Timestamp in ms to get aggregate trades until INCLUSIVE.
        """
        try:
            records = self._client.query_kline(symbol=pair, interval=self.convert_interval(interval),
                limit=kwargs.get("limit"), from_time=kwargs.get("start_time"))
        except Exception as e:
            print(e)
            return []

        candles = []
        for record in records["result"]:
            # cast values to proper types
            updated_record = [BYBIT_KLINE_SPEC[list(BYBIT_KLINE_SPEC)[index]](list(record.values())[index])
                for index in range(0, len(BYBIT_KLINE_SPEC))]

            # convert the Binance klines record to a generic OHLCV record
            candles.append(dict(zip(OHLCV_SPEC, updated_record[2:])))

        return candles
