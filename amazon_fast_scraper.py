import requests
from bs4 import BeautifulSoup

def scrape_amazon_fast(url):
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/115.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "DNT": "1",
        "Connection": "keep-alive",
    }

    try:
        response = session.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # ✅ Extract product name
        product_name_tag = soup.select_one("#productTitle")
        product_name = product_name_tag.get_text(strip=True) if product_name_tag else "Product Not Found"

        # ✅ Extract price from multiple selectors
        price_selectors = [
            ".a-price .a-offscreen",
            "#priceblock_ourprice",
            "#priceblock_dealprice",
            "span.a-price-whole"
        ]
        product_price = "Price Not Found"
        for selector in price_selectors:
            price_tag = soup.select_one(selector)
            if price_tag and price_tag.get_text(strip=True):
                product_price = price_tag.get_text(strip=True).replace("₹", "").replace(",", "")
                break

        # ✅ If Amazon blocked request, response may contain captcha
        if "Enter the characters you see below" in response.text or product_name == "Product Not Found":
            print("⚠️ Amazon blocked request, consider Selenium mode...")
        
        return product_name, product_price

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error scraping Amazon: {e}")
        return "Product Not Found", "Price Not Found"
