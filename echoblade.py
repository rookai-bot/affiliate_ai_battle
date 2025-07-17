# EchoBlade: Shadow AI for product research & blog writing

import json
import random
from datetime import datetime

# Simulated eBay product list (can later be pulled from a live API)
PRODUCTS = [
    {
        "title": "Adjustable Dumbbell Set - 44lb",
        "link": "https://www.ebay.com/itm/example1",
        "image": "https://i.ebayimg.com/images/example1.jpg",
        "category": "Fitness"
    },
    {
        "title": "Resistance Bands Workout Kit",
        "link": "https://www.ebay.com/itm/example2",
        "image": "https://i.ebayimg.com/images/example2.jpg",
        "category": "Home Gym"
    },
    {
        "title": "Smart Fitness Watch - Heart Rate & Steps",
        "link": "https://www.ebay.com/itm/example3",
        "image": "https://i.ebayimg.com/images/example3.jpg",
        "category": "Wearables"
    }
]

# AI-style product blurb generator
def generate_blurb(product):
    blurbs = [
        f"Level up your training with the {product['title']} — strength, style, and smart gains in one.",
        f"This {product['title']} is a top pick for crushing home workouts. No gym, no excuses.",
        f"Boost your hustle with the {product['title']}. Sleek, powerful, and built for warriors."
    ]
    return random.choice(blurbs)

# Create blog post
def create_blog_post(product):
    date_str = datetime.now().strftime("%Y-%m-%d")
    post = f"""
<h2>{product['title']}</h2>
<img src="{product['image']}" alt="{product['title']}" width="300">
<p><strong>Category:</strong> {product['category']}</p>
<p>{generate_blurb(product)}</p>
<p><a href="{product['link']}" target="_blank">🔗 Check it out on eBay</a></p>
<hr>
"""
    return post

# Create Shadow blog content and drop intelligence
selected = random.sample(PRODUCTS, 2)
blog_html = "\n".join([create_blog_post(p) for p in selected])

intel = [{
    "title": p['title'],
    "link": p['link'],
    "image": p['image'],
    "blurb": generate_blurb(p),
    "category": p['category']
} for p in selected]

# Save blog HTML
with open("blog/index.html", "w", encoding="utf-8") as f:
    f.write(f"""
<!DOCTYPE html>
<html>
<head>
  <title>EchoBlade Daily Drops</title>
  <meta charset="UTF-8">
  <style>
    body {{ font-family: sans-serif; max-width: 700px; margin: auto; padding: 20px; }}
    h2 {{ color: #0f0f0f; }}
    img {{ border-radius: 10px; }}
  </style>
</head>
<body>
  <h1>🕶 EchoBlade Intel Report – {datetime.now().strftime('%B %d, %Y')}</h1>
  {blog_html}
</body>
</html>
""")

# Save product intel for Prime
with open("intel/intel.json", "w", encoding="utf-8") as f:
    json.dump(intel, f, indent=2)

print("✅ EchoBlade has completed today’s drop.")
