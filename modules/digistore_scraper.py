import json
import random
import requests
from bs4 import BeautifulSoup
from pathlib import Path

AFFILIATE_ID = "Rookai"  # Your Digistore24 ID
SAVE_PATH = Path("intel/intel.json")
BASE_URL = "https://www.digistore24.com/en/category/fitness"  # You can change the category

def fetch_products():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(BASE_URL, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    product_cards = soup.select(".product-box")  # This is their card class

    results = []
    for card in product_cards:
        try:
            title = card.select_one(".product-box__title").text.strip()
            link = card.select_one("a")["href"]
            full_link = f"{link}?aff={AFFILIATE_ID}"
            image_tag = card.select_one("img")
            image = image_tag["src"] if image_tag else ""

            results.append({
                "title": title,
                "link": full_link,
                "image": image,
                "category": "Fitness"
            })
        except Exception as e:
            continue

    return random.sample(results, min(3, len(results)))  # Pick up to 3 products

def save_intel(products):
    SAVE_PATH.parent.mkdir(exist_ok=True)
    with open(SAVE_PATH, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=2)
    print(f"✅ Saved {len(products)} products to {SAVE_PATH}")

def start_scraper():
    print("🕵️ EchoBlade is scraping public Digistore24 marketplace...")
    products = fetch_products()
    save_intel(products)

if __name__ == "__main__":
    start_scraper()
