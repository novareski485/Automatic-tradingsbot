import numpy as np
import pandas as pd

def compute_ema(prices, span=10):
    return pd.Series(prices).ewm(span=span, adjust=False).mean()

def compute_rsi(prices, period=14):
    delta = np.diff(prices)
    up = np.where(delta > 0, delta, 0)
    down = np.where(delta < 0, -delta, 0)

    roll_up = pd.Series(up).rolling(period).mean()
    roll_down = pd.Series(down).rolling(period).mean()

    rs = roll_up / roll_down
    rsi = 100.0 - (100.0 / (1.0 + rs))
    return rsi

def analyze_trend(price_series):
    if len(price_series) < 20:
        return "UNKNOWN"  # Not enough data

    ema = compute_ema(price_series)
    rsi = compute_rsi(price_series)

    ema_slope = ema.iloc[-1] - ema.iloc[-5]
    rsi_latest = rsi.iloc[-1]

    if ema_slope > 0 and rsi_latest > 60:
        return "BULLISH"
    elif ema_slope < 0 and rsi_latest < 40:
        return "BEARISH"
    else:
        return "NEUTRAL"
