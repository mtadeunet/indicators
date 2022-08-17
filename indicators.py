
def rsi(df, rsi_ema_count):
    close = df.close
    delta = close.diff()

    up = delta.clip(lower=0).ewm(span=rsi_ema_count).mean()
    down = delta.clip(upper=0).abs().ewm(span=rsi_ema_count).mean()

    rs = up / down
    df["rsi"] = 100.0 - (100.0 / (1.0 + rs))

    return df
