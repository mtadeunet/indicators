import pandas
import pandas_ta as ta
import indicators
from config import settings
from client.factory import ClientFactory
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


# Get OHLCV records
with ClientFactory(settings) as client:
    ohlcv_settings = settings["ohlcv"]
    candles = client.ohlcv(ohlcv_settings["pair"], ohlcv_settings["interval"],
        start_time=ohlcv_settings["start_time"], end_time=ohlcv_settings["end_time"])

    # Create a Pandas DataFrame
    df = pandas.DataFrame(candles)

    # calculate the RSI data
    rsi1 = indicators.rsi(df.close, settings["rsi_ema_count"])
    rsi2 = df.ta.rsi(length=settings["rsi_ema_count"])      # for testing purposes

    # print(rsi1)
    print(rsi1 - rsi2) # should result in a zero vector

    # TODO: Generate plot data/image
    # TODO: Generate artifacts that signal position entries and exits
    # TODO: Mark the position entries and exits with the Closed P&L result
    # TODO: Detect divergencies between the price and the rsi movement
    # TODO: Make tests
    # TODO: Remove 'spec' dependency from config.py

    rsi1.plot.line(x="id", y="rsi")
    plt.show()

    # print(f"RSI:\n{df}")