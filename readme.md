# 🛒 Price Monitoring Tool

This Python project tracks product prices from **Amazon** and **Flipkart**, saves them to a CSV file, and sends email notifications for:
- Start of monitoring
- Price drops

---

## 📂 Project Structure
```
price_monitor_project/
│── main.py
│── amazon_fast_scraper.py
│── flipkart_fast_scraper.py
│── email_notification.py
│── price_history.csv
│── requirements.txt
│── README.md
```
---

## ⚙️ Installation

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
---

## ▶️ Run the Application
```bash
python main.py
```
---

## 📜 View Price History
```bash
python main.py --show-prices
```
---

## 🔧 Configuration
- **Product URLs:** Set inside `main.py` or pass as command-line arguments:
```bash
python main.py <Amazon_URL> <Flipkart_URL>
```
- **Email notifications:** Configure your sender email & app password in `email_notification.py`.

---

## ✅ Sample Output
```
🔎 Starting fast price monitoring...

Amazon → 📦 Apple iPhone 15 (128 GB) - Blue | 💰 59999.00
Flipkart → 📦 Apple iPhone 15 (Blue, 128 GB) | 💰 64900
✅ Email sent successfully!

--- Price Check Completed ---
⏳ Waiting 12 hours before next check...
```
