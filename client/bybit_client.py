from pybit.spot import HTTP
from specs import INTERVALS, OHLCV_SPEC
from client.base import ClientBase


BYBIT_KLINE_SPEC = {
    "start_time": int,
    "open": float,
    "high": float,
    "low": float,
    "close": float,
    "volume": float,
    "end_time": int,
    "quote_asset_volume": float,
    "trades": int,
    "taker_base_volume": float,
    "taker_quote_volume": float
}


class ByBit(ClientBase):
    def __init__(self):
        super().__init__(max_kline_records=200)
        self._client = HTTP(endpoint="https://api-testnet.bybit.com")

    def convert_interval(self, interval: INTERVALS):
        mapping = {
            "Minutes1": "1m",
            "Minutes5": "5m",
            "Minutes30": "30m",
            "Hours1": "1h",
            "Hours4": "4h",
            "Hours12": "12h",
            "Days1": "1d",
            "Week1": "1w",
            "Month1": "1M"
        }

        return mapping[interval.name]

    def _do_ohlcv(self, pair: str, interval: INTERVALS, **kwargs):
        """Get OHLCV values
        Args:
            symbol (str): the trading pair
            interval (INTERVALS): the interval of kline
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
            updated_record = [BYBIT_KLINE_SPEC[list(BYBIT_KLINE_SPEC)[index]](record[index])
                for index in range(0, len(BYBIT_KLINE_SPEC))]

            # convert the Binance klines record to a generic OHLCV record
            candles.append(dict(zip(OHLCV_SPEC, updated_record)))

        return candles

    def trades(self):
        pass
