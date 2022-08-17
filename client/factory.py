from client.binance_client import Binance
from client.bybit_client import ByBit

class ClientFactory:
    def __init__(self, settings):
        if settings["client"] == "binance":
            self._client = Binance()
        elif settings["client"] == "bybit":
            self._client = ByBit()

    def __enter__(self):
        return self._client

    def __exit__(self, type, value, traceback):
        pass
