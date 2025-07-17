import json
import datetime
import requests

# Load Digistore24 affiliate products
with open("intel/intel.json", "r") as f:
    products = json.load(f)

# Generate blog HTML content
html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>EchoBlade Affiliate Picks</title>
    <meta charset="UTF-8">
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: #121212;
            color: #f1f1f1;
            padding: 20px;
        }}
        h1 {{
            color: #00ffd5;
        }}
        .product {{
            margin-bottom: 30px;
            padding: 20px;
            border: 1px solid #333;
            border-radius: 10px;
            background: #1e1e1e;
        }}
        .category {{
            color: #aaa;
            font-style: italic;
        }}
        a {{
            color: #00ffd5;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <h1>EchoBlade's Latest Affiliate Drops</h1>
    <p><em>Updated: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</em></p>
"""

for p in products:
    html += f"""
    <div class="product">
        <h2>{p["name"]}</h2>
        <p class="category">Category: {p["category"]}</p>
        <p>{p["description"]}</p>
        <p><a href="{p["link"]}" target="_blank">🔗 Check it out</a></p>
    </div>
    """

html += "</body></html>"

# Save to blog
with open("blog/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ Saved {len(products)} Digistore24 products to blog/index.html")

# Trigger Netlify deploy hook
hook_url = "https://api.netlify.com/build_hooks/686bc19907d2f35a66882f94"
try:
    r = requests.post(hook_url)
    if r.status_code == 200:
        print("🚀 Triggered Netlify redeploy")
    else:
        print("❌ Netlify hook failed")
except Exception as e:
    print(f"⚠️ Deploy error: {e}")
