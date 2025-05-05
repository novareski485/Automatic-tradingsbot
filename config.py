# config.py

# GMGN API Configuration
GMGN_API_KEY = "your_gmgn_api_key"
GMGN_API_URL = "https://api.gmgn.ai/v1"
WALLET_ADDRESS = "your_wallet_address"

# Dexscreener API Configuration
DEXSCR_API_URL = "https://api.dexscreener.com/v1"

# Trading Strategy Configuration
INSIDER_MIN_BUY_USD = 1000  # Minimum USD for an insider buy to trigger action
INSIDER_MIN_SELL_USD = 1000
INSIDER_POLL_INTERVAL = 10  # seconds

# Social Media Validation
SOCIAL_VALID_MIN_LINKS = 1  # Threshold for social media presence

# Database configuration
DATABASE_URL = "postgresql://user:password@localhost/dbname"
