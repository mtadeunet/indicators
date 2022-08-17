import pandas
from config import settings
from binance_client import Binance
import indicators

candles = Binance(settings).ohlcv(settings["pair"], settings["interval"], limit=settings["candle_count"])
df = pandas.DataFrame(candles)

indicators.rsi(df, settings["rsi_ema_count"])

print(f"RSI: {df.rsi}")