import time
import csv
import sys
from datetime import datetime
from amazon_fast_scraper import scrape_amazon_fast
from flipkart_fast_scraper import scrape_flipkart_fast
from email_notification import send_email  # Assuming this is working

# CSV file
CSV_FILE = "price_history.csv"

# Check if user wants to view stored prices
if "--show-prices" in sys.argv:
    try:
        with open(CSV_FILE, "r") as f:
            print("\n📜 Price History:\n")
            print(f.read())
    except FileNotFoundError:
        print("⚠️ No price history found yet.")
    sys.exit()

# Take product URLs from CLI or fallback to defaults
if len(sys.argv) >= 3:
    AMAZON_URL = sys.argv[1]
    FLIPKART_URL = sys.argv[2]
else:
    AMAZON_URL = "https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX2F5QT"
    FLIPKART_URL = "https://www.flipkart.com/apple-iphone-15-blue-128-gb/p/itmbf14ef54f645d?pid=MOBGTAGPAQNVFZZY"

# Store last known price to detect drops
last_amazon_price = None
last_flipkart_price = None
email_sent = False  # To ensure start email is sent only once

def save_to_csv(platform, name, price):
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), platform, name, price])

def monitor_prices():
    global last_amazon_price, last_flipkart_price, email_sent

    print("\n🔎 Starting fast price monitoring...\n")

    try:
        pname_a, price_a = scrape_amazon_fast(AMAZON_URL)
        pname_f, price_f = scrape_flipkart_fast(FLIPKART_URL)

        print(f"Amazon → 📦 {pname_a} | 💰 {price_a}")
        print(f"Flipkart → 📦 {pname_f} | 💰 {price_f}")

        # Save to CSV
        save_to_csv("Amazon", pname_a, price_a)
        save_to_csv("Flipkart", pname_f, price_f)

        # Send email at start of monitoring
        if not email_sent:
            send_email("Monitoring Started", f"Tracking prices:\nAmazon: {price_a}\nFlipkart: {price_f}")
            email_sent = True

        # Send email on price drop
        if last_amazon_price and price_a != "Price Not Found" and float(price_a) < float(last_amazon_price):
            send_email("Price Drop Alert - Amazon", f"New price: {price_a}\nOld price: {last_amazon_price}")
        if last_flipkart_price and price_f != "Price Not Found" and float(price_f) < float(last_flipkart_price):
            send_email("Price Drop Alert - Flipkart", f"New price: {price_f}\nOld price: {last_flipkart_price}")

        last_amazon_price = price_a if price_a != "Price Not Found" else last_amazon_price
        last_flipkart_price = price_f if price_f != "Price Not Found" else last_flipkart_price

    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

    print("\n--- Price Check Completed ---\n")
    print("⏳ Waiting 12 hours before next check...")

if __name__ == "__main__":
    # Create CSV with headers if not exists
    try:
        with open(CSV_FILE, "x", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "Platform", "Product Name", "Price"])
    except FileExistsError:
        pass

    while True:
        monitor_prices()
        time.sleep(12 * 60 * 60)  # 12 hours = 43200 seconds
