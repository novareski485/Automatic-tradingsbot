from gmgn_trader import place_buy
from insider_watch import stream_insider_activity
from trend_analyzer import analyze_trend
from social_checker import check_social_presence

def handle_insider_trade(trade):
    print(f"Significant insider trade detected: {trade}")

if __name__ == "__main__":
    # Start the insider trade monitoring in a separate thread
    stream_insider_activity(handle_insider_trade, poll_interval=10)
