# 📌 Price Monitoring Application

## 📝 Project Overview
The **Price Monitoring Application** is a Python-based tool that automatically fetches product prices from **Amazon** and **Flipkart**, stores them in a CSV file for history tracking, and sends **email notifications** to the user whenever:
- ✅ Price monitoring starts  
- ✅ A **price drop** is detected  

This application helps users **track online prices** efficiently without manual checking.

---

## ⚙️ Features
- 🔹 **Fetch prices** from Amazon and Flipkart using web scraping (Requests + BeautifulSoup).  
- 🔹 **Stores prices with timestamps** in a CSV file.  
- 🔹 **Email alerts** for price drops and process start.  
- 🔹 **CLI option** to view stored price history instantly.  
- 🔹 **Scheduled execution** every 12 hours (can be adjusted).  

---

## 📂 Project Structure
price_monitor_project/
│
├── price_monitor/
│ ├── main.py # Main script (scheduler + execution)
│ ├── amazon_fast_scraper.py # Fetches Amazon product details
│ ├── flipkart_fast_scraper.py # Fetches Flipkart product details
│ ├── email_notification.py # Sends email notifications
│ ├── price_history.csv # Stores fetched prices with timestamps
│ ├── requirements.txt # Required dependencies


---

## 🚀 How to Run
### 1️⃣ Install dependencies:
```bash
pip install -r requirements.txt

2️⃣ Run the application:
python main.py

3️⃣ View saved price history anytime:
python main.py --show-prices

🔧 Configuration
Product URLs: Set inside main.py or pass as command-line arguments:
python main.py <Amazon_URL> <Flipkart_URL>
Email notifications: Configure your sender email & app password in email_notification.py.

✅ Sample Output
🔎 Starting fast price monitoring...

Amazon → 📦 Apple iPhone 15 (128 GB) - Blue | 💰 59999.00
Flipkart → 📦 Apple iPhone 15 (Blue, 128 GB) | 💰 64900
✅ Email sent successfully!

--- Price Check Completed ---
⏳ Waiting 12 hours before next check...

