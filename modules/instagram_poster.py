import os
from instagrapi import Client

def post_to_instagram(captions, products, image_paths):
    username = os.getenv("INSTAGRAM_USERNAME")
    password = os.getenv("INSTAGRAM_PASSWORD")

    if not username or not password:
        raise ValueError("Instagram username or password not found in environment variables.")

    cl = Client()
    cl.login(username, password)

    for cap, p, img_path in zip(captions, products, image_paths):
        full_caption = f"{cap}\n\nLink: {p['link']}"
        cl.photo_upload(img_path, full_caption)
        print(f"[instagram_poster] ✅ Posted: {p['title']}")
