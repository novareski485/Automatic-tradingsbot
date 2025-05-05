# Memecoin Trading Bot

## Overview

This bot monitors memecoins, performs trend analysis, places trades, and tracks insider activity.

## Requirements

- Docker
- Docker Compose
- Python 3.9+
- PostgreSQL (if using database)

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/trading-bot.git
    cd trading-bot
    ```

2. Set your environment variables in `config.py`.

3. Build and run the bot using Docker Compose:
    ```bash
    docker-compose up -d
    ```

## Monitoring Logs

To view the logs of the trading bot:
```bash
docker logs -f trading-bot-container
