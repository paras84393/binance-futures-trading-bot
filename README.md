# Binance Futures Testnet Trading Bot

A simple Python CLI-based trading bot that places **MARKET** and **LIMIT** orders on **Binance Futures Testnet (USDT-M)**.

This project demonstrates API integration, structured Python code, logging, and error handling.

---

## Features

* Place **MARKET** orders
* Place **LIMIT** orders
* Supports **BUY** and **SELL** sides
* Command Line Interface using `argparse`
* Structured code with separate modules
* Logging of API requests, responses, and errors
* Input validation and exception handling

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance API client wrapper
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation
│   └── logging_config.py  # Logging setup
│
├── cli.py                 # CLI entry point
├── requirements.txt
├── trading_bot.log
└── README.md
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone <YOUR_GITHUB_REPO_LINK>
cd trading_bot
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Create a `.env` file

Add your Binance Futures Testnet API credentials:

```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_secret_key
```

---

## Running the Bot

### MARKET Order Example

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

### LIMIT Order Example

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 70000
```

---

## Output

The CLI prints:

* Order request summary
* Order response details
* Success or failure message

Example:

```
====== ORDER SUMMARY ======
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.002

====== RESPONSE ======
OrderId: 123456789
Status: FILLED
ExecutedQty: 0.002
AvgPrice: 67000

✅ Order placed successfully
```

---

## Logging

All API requests, responses, and errors are logged to:

```
trading_bot.log
```

Example log entry:

```
INFO | Order Request: BTCUSDT BUY MARKET qty=0.002
INFO | Order Response: {...}
ERROR | APIError(code=-2019): Margin is insufficient
```

---

## Assumptions

* Binance Futures Testnet account is active
* API credentials are stored securely in `.env`
* Minimum order size requirements follow Binance Futures rules

---

## Tech Stack

* Python 3.x
* python-binance
* argparse
* logging
* python-dotenv

---

## Author

Paras Jain
