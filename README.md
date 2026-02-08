# 📈 Stock Market WhatsApp Alert App in Python

This Python script monitors a stock (e.g., Tesla) and sends **WhatsApp/SMS alerts** when price changes significantly.  
It also fetches relevant news for the stock and includes it in the alert.

---

## 🛠️ Technologies Used

- Python 3.11
- requests
- python-dotenv
- twilio
- Docker (optional containerization)

---

## 🚀 Features

- Fetches daily stock prices via Alpha Vantage API
- Sends WhatsApp/SMS alerts via Twilio
- Fetches latest news via NewsAPI
- Processes percentage change to trigger alerts
- Environment variables for API keys

---

## 📂 Project Structure
```bash
stock-alert/
│
├── main.py
├── .env
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## ⚡ Setup and Usage

1. Install dependencies:

```bash
git clone https://github.com/Fayyaz6137/Stock-Market-WhatsApp-Alert.git

cd stock-market-whatsapp-alert

pip install -r requirements.txt
```

2. Create a .env file in the project root:

```bash
STOCK_API_KEY=your_alpha_vantage_key

NEWS_API_KEY=your_newsapi_key

TWELLO_ACCOUNT_SID=your_twilio_sid

TWELLO_AUTH_TOKEN=your_twilio_auth_token
```

3. Run the script locally:

```bash
python main.py
```

---

## 🐳 Run With Docker

```bash
docker compose up --build
```
The script reads .env variables for API keys.

---


## 📚 What I Learned

* Working with stock APIs
* Sending WhatsApp/SMS via Twilio
* Parsing JSON data
* Fetching news with REST APIs
* Docker containerization for Python scripts

---
## 🔮 Future Improvements

* Schedule periodic alerts (cron or sleep loop)
* Support multiple stocks
* Send alerts via email in addition to WhatsApp
* Log all alerts to a file or database
