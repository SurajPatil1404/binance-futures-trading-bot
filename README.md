# 🚀 Binance Futures Testnet Trading Bot

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Binance](https://img.shields.io/badge/Binance-Futures_Testnet-yellow)

A modular Python-based trading bot for the **Binance Futures Testnet (USDT-M)** built using Python. The project demonstrates algorithmic trading fundamentals, API integration, order execution, validation, logging, and clean software architecture in a safe simulated trading environment.

The bot supports both **Market** and **Limit** orders, provides structured logging, validates user inputs, and includes an enhanced command-line interface for improved usability.

---

# ✨ Features

✅ Binance Futures Testnet Integration

✅ Market Orders (BUY / SELL)

✅ Limit Orders (BUY / SELL)

✅ Symbol Validation

✅ Input Validation

✅ Structured Logging

✅ Order Request Summaries

✅ Order Response Details

✅ Environment Variable Security

✅ Modular & Scalable Architecture

✅ Exception Handling

✅ Enhanced CLI UX (Bonus Feature)

---

# 🎁 Bonus Feature

## Enhanced CLI UX

To improve user experience, the application includes an interactive menu-driven CLI built using **Rich**.

Run:

```bash
python3 cli.py
```

Users can:

* Select Market Orders
* Select Limit Orders
* Enter Symbol, Side, Quantity, and Price interactively
* Receive clear prompts and validation feedback

Example:

```text
🚀 Binance Futures Testnet Trading Bot

1. Market Order
2. Limit Order
3. Exit
```

This reduces input errors and makes the application easier to use.

---

# 🛠️ Tech Stack

* Python 3.x
* Binance Futures API
* Click
* Rich
* python-dotenv
* Logging
* REST APIs

---

# 📂 Project Structure

```text
binance-futures-trading-bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── validators.py
│   ├── orders.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/SurajPatil1404/binance-futures-trading-bot.git
cd binance-futures-trading-bot
```

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate:

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configuration

Create a `.env` file in the project root:

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

⚠️ Never commit your API credentials or `.env` file to GitHub.

---

# ▶️ Running the Bot

## Interactive Mode

```bash
python3 cli.py
```

## Command-Line Mode

### Market Order Example

```bash
python3 cli.py \
--symbol BTCUSDT \
--side BUY \
--order-type MARKET \
--quantity 0.001
```

### Limit Order Example

```bash
python3 cli.py \
--symbol BTCUSDT \
--side SELL \
--order-type LIMIT \
--quantity 0.001 \
--price 200000
```

---

# 📋 Order Output

The application displays a clear execution summary for every order.

## Order Request Summary

* Symbol
* Side
* Order Type
* Quantity
* Price (for LIMIT orders)

## Order Response Details

* Order ID
* Status
* Executed Quantity
* Average Price

Example:

```text
📋 Order Request Summary
Symbol: BTCUSDT
Side: BUY
Order Type: MARKET
Quantity: 0.001

📊 Order Response Details
Order ID: 13686607890
Status: NEW
Executed Quantity: 0.0000
Average Price: 0.00

✅ Order placed successfully
```

---

# 📝 Logging

Execution logs are stored in:

```text
logs/trading.log
```

The log file includes:

* MARKET Order Executions
* LIMIT Order Executions
* API Requests
* API Responses
* Success Messages
* Error Details

Sample logs from both MARKET and LIMIT orders are included to satisfy assignment requirements.

---

# 📊 Learning Objectives

This project helped explore:

* Financial APIs
* Algorithmic Trading Concepts
* Python Project Architecture
* Logging & Debugging
* Secure Credential Management
* Git & GitHub Best Practices
* CLI Application Development

---

# 🔒 Security

* API keys are stored using environment variables.
* Sensitive files are excluded via `.gitignore`.
* No credentials are stored in source code.
* Designed exclusively for Binance Futures Testnet usage.

---

# 🎯 Future Improvements

* Trading Strategies
* Real-Time Market Data Integration
* AI-Based Trade Signals
* Performance Dashboard
* Unit Testing
* Stop-Loss & Take-Profit Orders
* Web-Based Dashboard

---

# 👨‍💻 Author

## Suraj Patil

**B.Tech Computer Science (AI & ML)**
Newton School of Technology (NST), ADYPU

Passionate about AI, Software Development, FinTech, and building real-world projects that solve practical problems.

---

# ⭐ Assignment Highlights

* Binance Futures Testnet Integration
* Market Order Execution
* Limit Order Execution
* BUY / SELL Support
* Input Validation
* Structured Logging
* Exception Handling
* Order Request Summaries
* Order Response Details
* Environment Variable Security
* Enhanced CLI UX (Bonus Feature)
* Clean GitHub Repository Structure

---

⭐ If you found this project useful, consider giving it a star!
