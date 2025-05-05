import requests
from config import GMGN_API_KEY, GMGN_API_URL, WALLET_ADDRESS

HEADERS = {
    "Authorization": f"Bearer {GMGN_API_KEY}",
    "Content-Type": "application/json"
}

def place_buy(mint_address, amount_usd):
    payload = {
        "wallet": WALLET_ADDRESS,
        "mint": mint_address,
        "amountUsd": amount_usd,
        "side": "buy"
    }
    return send_order(payload)

def place_sell(mint_address, amount_percent=100):
    payload = {
        "wallet": WALLET_ADDRESS,
        "mint": mint_address,
        "amountPercent": amount_percent,
        "side": "sell"
    }
    return send_order(payload)

def send_order(payload):
    try:
        response = requests.post(f"{GMGN_API_URL}/trade", json=payload, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"[GMGN] Order failed: {e}")
        return None
