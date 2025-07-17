from instagrapi import Client

username = "agen.t8274"
password = "oratile73"

# Login to Instagram
cl = Client()
cl.login(username, password)

# Post a photo
media = cl.photo_upload(
    "product1.jpg", 
    "🔥 Boost your gains with this top fitness product!\n#fitness #homegym #affiliate #gymgear #instaprime"
)

print("✅ Image uploaded successfully.")
