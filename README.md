# 🚀 Binance Futures Testnet Trading Bot

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Binance](https://img.shields.io/badge/Binance-Futures_Testnet-yellow)

A modular Python-based trading bot for the **Binance Futures Testnet**, built to explore algorithmic trading, API integration, order execution, and trading system architecture in a safe simulated environment.

---

## ✨ Features

✅ Binance Futures Testnet Integration

✅ Market Orders

✅ Limit Orders

✅ Symbol Validation

✅ Order Validation

✅ Structured Logging

✅ Environment Variable Security

✅ Modular & Scalable Architecture

✅ Error Handling

---

## 🎁 Bonus Feature Implemented

### Enhanced CLI UX

To improve usability, the bot includes an interactive command-line interface built using **Rich**.

Instead of remembering long command-line arguments, users can simply run:

```bash
python3 cli.py
```

and choose options from a menu:

```text
🚀 Binance Futures Testnet Trading Bot

1. Market Order
2. Limit Order
3. Exit
```

The interface then prompts the user for:

* Trading Symbol
* Order Side (BUY/SELL)
* Quantity
* Price (for Limit Orders)

This makes the application beginner-friendly and reduces user input errors.

---

## 🛠️ Tech Stack

* 🐍 Python
* 📈 Binance Futures API
* ⚡ Click
* 🎨 Rich
* 🔐 python-dotenv
* 📝 Logging
* 🌐 REST APIs

---

## 📂 Project Structure

```text
binance-futures-trading-bot/
│
├── bot/
│   ├── client.py
│   ├── validators.py
│   ├── orders.py
│   ├── logging_config.py
│   └── __init__.py
│
├── cli.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/SurajPatil1404/binance-futures-trading-bot.git
cd binance-futures-trading-bot
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

Create a `.env` file in the project root:

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

⚠️ Never commit your `.env` file to GitHub.

---

## ▶️ Running the Bot

### Interactive Mode

```bash
python3 cli.py
```

### Command-Line Mode

#### Market Order

```bash
python3 cli.py \
--symbol BTCUSDT \
--side BUY \
--order-type MARKET \
--quantity 0.001
```

#### Limit Order

```bash
python3 cli.py \
--symbol BTCUSDT \
--side BUY \
--order-type LIMIT \
--quantity 0.001 \
--price 50000
```

---

## 📊 Learning Objectives

This project helped me explore:

* Financial APIs
* Algorithmic Trading Concepts
* Python Project Architecture
* Logging & Debugging
* Secure Credential Management
* Git & GitHub Best Practices
* CLI Application Development

---

## 🔒 Security

* API keys are stored using environment variables.
* Sensitive files are excluded using `.gitignore`.
* Designed exclusively for Binance Futures **Testnet** usage.
* No credentials are stored in source code.

---

## 🎯 Future Improvements

* 📉 Trading Strategies
* 📊 Real-Time Market Data Integration
* 🤖 AI-Based Trade Signals
* 📈 Performance Dashboard
* 🧪 Unit Testing
* 🛑 Stop-Loss & Take-Profit Orders
* 📱 Web-Based Dashboard

---

## 👨‍💻 Author

### Suraj Patil

**B.Tech Computer Science (AI & ML)**
Newton School of Technology, ADYPU

Passionate about AI, Software Development, FinTech, and building real-world projects that solve practical problems.

---

## ⭐ Assignment Highlights

* Binance Futures Testnet Integration
* Market & Limit Order Execution
* Validation Layer
* Logging Layer
* Environment Variable Security
* Enhanced CLI UX Bonus Feature
* Clean GitHub Repository Structure

---

⭐ If you found this project useful, consider giving it a star!
