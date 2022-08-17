from binance.spot import Spot
from specs import OHLCV_SPEC

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

class Binance:
    def __init__(self, settings):
        self._client = Spot()

    def ohlcv(self, pair: str, interval: str, **kwargs):
        """Get OHLCV values
        Args:
            symbol (str): the trading pair
            interval (str): the interval of kline, e.g 1m, 5m, 1h, 1d, etc.
        Keyword Args:
            limit (int, optional): limit the results. Default 500; max 1000.
            startTime (int, optional): Timestamp in ms to get aggregate trades from INCLUSIVE.
            endTime (int, optional): Timestamp in ms to get aggregate trades until INCLUSIVE.
        """
        try:
            records = self._client.klines(pair, interval,
                limit=kwargs.get("limit"), startTime=kwargs.get("startTime"), endTime=kwargs.get("endTime"))
        except:
            return []

        candles = []
        for record in records:
            # cast values to proper types
            updated_record = [BINANCE_KLINE_SPEC[list(BINANCE_KLINE_SPEC)[index]](record[index])
                for index in range(0, len(BINANCE_KLINE_SPEC))]

            # convert the Binance klines record to a generic OHLCV record
            candles.append(dict(zip(OHLCV_SPEC, updated_record)))

        return candles
