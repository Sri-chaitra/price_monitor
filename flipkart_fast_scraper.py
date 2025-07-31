import requests
from bs4 import BeautifulSoup

def scrape_flipkart_fast(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/115.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract product name
        product_name = soup.select_one("span.VU-ZEz")  # Updated selector
        product_name = product_name.get_text(strip=True) if product_name else "Product Not Found"

        # Extract price
        price_tag = soup.select_one("div.Nx9bqj.CxhGGd")
        product_price = price_tag.get_text(strip=True).replace("₹", "").replace(",", "") if price_tag else "Price Not Found"

        return product_name, product_price

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error scraping Flipkart: {e}")
        return "Product Not Found", "Price Not Found"
