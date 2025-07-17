import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.product_finder import find_products
from modules.content_creator import (
    make_instagram_captions,
    make_website_html,
    generate_image
)
from modules.instagram_poster import post_to_instagram
from modules.deployer import trigger_deploy

def run_instaprime():
    print("[InstaPrime] Starting daily cycle...")

    products = find_products()
    captions = make_instagram_captions(products)
    image_paths = [generate_image(p, i) for i, p in enumerate(products)]
    post_to_instagram(captions, products, image_paths)
    make_website_html(products, captions)
    trigger_deploy()

    print("[InstaPrime] ✅ Daily routine complete!")

if __name__ == "__main__":
    run_instaprime()
