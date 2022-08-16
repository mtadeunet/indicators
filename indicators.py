from binance.spot import Spot
import pandas
from config import settings

client = Spot()

kline = {
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

candles = []

for record in client.klines(settings["pair"], settings["interval"], limit=settings["candle_count"]):
    # cast values to proper types
    updated_record = [kline[list(kline)[index]](record[index])
        for index in range(0, len(kline))]

    # add the properly set dict to list
    candles.append(dict(zip(kline, updated_record)))

df = pandas.DataFrame(candles)

close = df.close
delta = close.diff()

up = delta.clip(lower=0).ewm(span=settings["rsi_ema_count"]).mean()
down = delta.clip(upper=0).abs().ewm(span=settings["rsi_ema_count"]).mean()

rs = up / down
df["rsi"] = 100.0 - (100.0 / (1.0 + rs))

print(f"RSI: {df.rsi}")

