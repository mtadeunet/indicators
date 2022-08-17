import pandas
from config import settings
from binance_client import Binance
from bybit_client import ByBit
import indicators

if settings["client"] == "binance":
    client = Binance(settings)
elif settings["client"] == "bybit":
    client = ByBit(settings)

candles = client.ohlcv(settings["pair"], settings["interval"],
    limit=settings["candle_count"], start_time=settings["start_time"])
df = pandas.DataFrame(candles)

indicators.rsi(df, settings["rsi_ema_count"])

print(f"RSI: {df.rsi}")