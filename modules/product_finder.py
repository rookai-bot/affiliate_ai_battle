# modules/product_finder.py

import requests
from bs4 import BeautifulSoup
from modules import content_creator
from modules import deployer
import modules.credentials as credentials


def find_products():
    try:
        print("[product_finder] Logging into Digistore24 and fetching products...")

        # Set up session
        session = requests.Session()
        login_url = "https://www.digistore24.com/signin"
        dashboard_url = "https://www.digistore24.com/en/home/affiliate/products"

        # Step 1: Get login page (to get any CSRF tokens or cookies)
        session.get(login_url)

        # Step 2: Log in
        payload = {
            "email": credentials.USERNAME,
            "password": credentials.PASSWORD
        }
        session.post(login_url, data=payload)

        # Step 3: Access product page (post-login)
        response = session.get(dashboard_url)
        response.raise_for_status()

        # Step 4: Parse products (example logic)
        soup = BeautifulSoup(response.text, "html.parser")
        product_elements = soup.select(".product-tile")  # Example selector, update if needed

        products = []
        for el in product_elements[:2]:  # Limit for testing
            title = el.select_one(".product-title").text.strip()
            link = el.select_one("a")['href']
            image = el.select_one("img")['src'] if el.select_one("img") else ""

            products.append({
                "title": title,
                "link": link,
                "image": image,
                "category": "General"
            })

        print("[product_finder] Fetched", len(products), "products.")
        return products

    except Exception as e:
        print("[❌ Error fetching Digistore24 products]", e)
        return []


def run():
    products = find_products()
    if products:
        content_creator.generate_website(products)
        deployer.trigger_deploy()
