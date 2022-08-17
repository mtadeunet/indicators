from specs import INTERVALS
import time

class ClientBase:
    def __init__(self, max_kline_records):
        self._max_kline_records = max_kline_records

    def _do_ohlcv(self, pair: str, interval: INTERVALS, **kwargs):
        raise Exception("Not implemented")

    def ohlcv(self, pair: str, interval: INTERVALS, **kwargs):
        """Get OHLCV values
        Args:
            symbol (str): the trading pair
            interval (INTERVALS): the interval of kline
        Keyword Args:
            limit (int, optional): limit the results. Default 500; max 1000.
            start_time (int, optional): Timestamp in ms to get aggregate trades from INCLUSIVE.
            end_time (int, optional): Timestamp in ms to get aggregate trades until INCLUSIVE.
        """
        limit = kwargs.get("limit", self._max_kline_records)
        if limit > self._max_kline_records:
            limit = self._max_kline_records

        end_time = kwargs.get("end_time", time.time())
        start_time = kwargs.get("start_time", end_time - interval * limit)

        necessary_records = int((end_time - start_time) / interval)

        candles = []
        while necessary_records:
            records = self._do_ohlcv(pair, interval, limit=min(necessary_records, limit), start_time=start_time, end_time=end_time)
            candles.extend(records)

            necessary_records = max(0, necessary_records - len(records))
            start_time += interval * len(records)

        return candles
