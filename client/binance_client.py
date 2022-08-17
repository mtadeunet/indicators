
from binance.spot import Spot
from specs import OHLCV_SPEC, INTERVALS
from client.base import ClientBase

BINANCE_KLINE_SPEC = {
    "open_time": int,
    "open": float,
    "high": float,
    "low": float,
    "close": float,
    "volume": float,
    "close_time": float,
    "quote_asset_volume": float,
    "number_of_trades": int,
    "taker_buy_base_asset_volume": float,
    "taker_buy_quote_asset_volume": float,
    "ignore": int,
}

class Binance(ClientBase):
    def __init__(self):
        super().__init__(max_kline_records=1000)
        self._client = Spot()

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
        try:
            records = self._client.klines(pair, self.convert_interval(interval),
                limit=kwargs.get("limit"), startTime=kwargs.get("start_time") * 1000, endTime=kwargs.get("end_time") * 1000)
        except Exception as e:
            print(e)
            return []

        candles = []
        for record in records:
            # cast values to proper types
            updated_record = [BINANCE_KLINE_SPEC[list(BINANCE_KLINE_SPEC)[index]](record[index])
                for index in range(0, len(BINANCE_KLINE_SPEC))]

            # convert the Binance klines record to a generic OHLCV record
            candles.append(dict(zip(OHLCV_SPEC, updated_record)))

        return candles

    def trades(self):
        pass
