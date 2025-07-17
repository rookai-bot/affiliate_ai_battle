import os
import json
from datetime import date

def make_blog_html(products):
    """
    Generate blog/index.html with all products as HTML posts.
    """
    today = date.today().isoformat()
    os.makedirs("blog", exist_ok=True)
    path = "blog/index.html"

    html = [
        "<!DOCTYPE html>",
        "<html><head>",
        f"<title>EchoBlade Daily Drops — {today}</title>",
        "<meta charset='UTF-8'>",
        "<style>",
        "body{font-family:sans-serif;max-width:800px;margin:auto;padding:20px;}",
        "h2{color:#336;}",
        "img{max-width:100%;border-radius:8px;}",
        "a{color:#06f;}",
        "</style>",
        "</head><body>",
        f"<h1>🧠 EchoBlade Intel Report — {today}</h1><hr>"
    ]
    for p in products:
        html += [
            "<div class='product'>",
            f"<h2>{p['title']}</h2>",
            f"<img src='{p['image']}' alt='{p['title']}' />",
            f"<p>{p['description']}</p>",
            f"<a href='{p['link']}' target='_blank'>🔗 View Product</a>",
            "<hr></div>"
        ]
    html += ["</body></html>"]

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(html))
    print(f"[content_creator] blog written to {path}")

def make_instagram_captions(products):
    """
    Generate Instagram captions for each product.
    Returns list of strings.
    """
    captions = []
    for p in products:
        cap = (
            f"🔥 {p['title']}\n"
            f"{p['description'][:80]}...\n"
            f"👉 {p['link']}\n"
            "#fitness #affiliatemarketing #homegym #health"
        )
        captions.append(cap)
    return captions

def make_website_html(products, captions):
    """
    Generate website/index.html with products and captions.
    """
    today = date.today().isoformat()
    os.makedirs("website", exist_ok=True)
    path = "website/index.html"

    html = [
        "<!DOCTYPE html>",
        "<html><head>",
        f"<title>InstaPrime Daily Deals — {today}</title>",
        "<meta charset='UTF-8'>",
        "<link rel='stylesheet' href='style.css'>",
        "</head><body>",
        f"<h1>🔥 InstaPrime Daily Deals — {today}</h1>",
        "<section id='products'>"
    ]
    for p, cap in zip(products, captions):
        html += [
            "<div class='product'>",
            f"<img src='{p['image']}' alt='{p['title']}' />",
            f"<h2>{p['title']}</h2>",
            f"<p>{cap.splitlines()[0]}</p>",
            f"<a href='{p['link']}' target='_blank'>Buy Now</a>",
            "</div>"
        ]
    html += ["</section></body></html>"]

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(html))
    print(f"[content_creator] website written to {path}")
from PIL import Image, ImageDraw, ImageFont
import textwrap

def generate_image(product, index=0):
    os.makedirs("images", exist_ok=True)
    img_path = f"images/generated_{index}.jpg"

    width, height = 720, 720
    img = Image.new("RGB", (width, height), color=(245, 245, 245))
    draw = ImageDraw.Draw(img)

    # Load font (fallback if not found)
    try:
        font_title = ImageFont.truetype("arial.ttf", 36)
        font_desc = ImageFont.truetype("arial.ttf", 24)
    except:
        font_title = ImageFont.load_default()
        font_desc = ImageFont.load_default()

    # Wrap and draw title
    title = textwrap.fill(product['title'], width=30)
    draw.text((40, 40), title, font=font_title, fill=(0, 0, 0))

    # Wrap and draw description
    desc = textwrap.fill(product['description'], width=40)
    draw.text((40, 200), desc, font=font_desc, fill=(60, 60, 60))

    img.save(img_path)
    return img_path
