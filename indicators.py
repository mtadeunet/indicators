
def rsi(df, length):
    close = df.close
    delta = close.diff()

    up = delta.clip(lower=0).ewm(span=length).mean()
    down = delta.clip(upper=0).abs().ewm(span=length).mean()

    rs = up / down
    df["rsi"] = 100.0 - (100.0 / (1.0 + rs))

    return df

def ema(length):
    pass

def stoch_rsi(length_rsi, length_stoch, smooth_k, smooth_d):
    pass