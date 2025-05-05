import time
import requests
from config import GMGN_API_URL, GMGN_API_KEY, INSIDER_MIN_BUY_USD, INSIDER_MIN_SELL_USD

HEADERS = {
    "Authorization": f"Bearer {GMGN_API_KEY}",
    "Content-Type": "application/json"
}

def fetch_insider_trades():
    try:
        resp = requests.get(f"{GMGN_API_URL}/insiders", headers=HEADERS)
        resp.raise_for_status()
        return resp.json().get("trades", [])
    except requests.RequestException as e:
        print(f"[InsiderWatch] Error fetching trades: {e}")
        return []

def is_significant_trade(trade):
    size = trade.get("amountUsd", 0)
    side = trade.get("side", "").lower()
    return (side == "buy" and size >= INSIDER_MIN_BUY_USD) or (side == "sell" and size >= INSIDER_MIN_SELL_USD)

def stream_insider_activity(notify_callback, poll_interval=10):
    seen_txids = set()
    while True:
        trades = fetch_insider_trades()
        for trade in trades:
            txid = trade.get("txid")
            if txid in seen_txids:
                continue
            seen_txids.add(txid)

            if is_significant_trade(trade):
                notify_callback(trade)

        time.sleep(poll_interval)
