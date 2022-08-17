from pandas import DataFrame

def rsi(close: DataFrame, length: int):
    up = close.diff()
    down = up.copy()

    up[up < 0] = 0
    down[down > 0] = 0

    up_mean = up.ewm(alpha=1/length, min_periods=length).mean()
    down_mean = down.ewm(alpha=1/length, min_periods=length).mean().abs()

    return 100 * up_mean / (up_mean + down_mean)

    return df

def ema(close: DataFrame, length):
    pass

def stoch_rsi(close: DataFrame, length: int, rsi_length: int, smooth_k, smooth_d):
    pass