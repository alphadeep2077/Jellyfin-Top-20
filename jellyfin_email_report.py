import requests
import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Config 
JELLYFIN_URL = "Your JellyFin-URL"
API_KEY = "Your API Key"
USER_ID = "Your User-id"
LIBRARY_ID = "Your Lib-id"
EMAIL = "Your-mail"
APP_PASSWORD = "Your google app password"

headers = {"X-Emby-Token": API_KEY}

# Fetch top 20 played items , you can change the limit if you want !!
params = {
    "ParentId": LIBRARY_ID,
    "Recursive": True,
    "SortBy": "PlayCount",
    "SortOrder": "Descending",
    "Fields": "PlayCount",
    "Limit": 20
}
response = requests.get(f"{JELLYFIN_URL}/Users/{USER_ID}/Items", headers=headers, params=params)
items = response.json().get("Items", [])

# Build HTML with CID image references , feel free to change the HTML code for better design !!
html = """
<html>
<head>
<style>
body { font-family: Arial, sans-serif; padding: 20px; background: #f4f4f4; }
.item { display: flex; align-items: center; margin-bottom: 20px; background: white; padding: 10px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
.item img { width: 80px; height: 80px; border-radius: 10px; margin-right: 15px; object-fit: cover; }
.title { font-size: 20px; font-weight: bold; margin-bottom: 20px; }
</style>
</head>
<body>
<div class="title">🎧 Top 20 Most Played Items ( Music Library)</div>
"""

# Compose the email
msg = MIMEMultipart("related")
msg["Subject"] = "🎶 Jellyfin Top Played Items"
msg["From"] = EMAIL
msg["To"] = EMAIL

alt_part = MIMEMultipart("alternative")
msg.attach(alt_part)

image_count = 0
for i, item in enumerate(items, 1):
    name = item.get("Name", "Unknown")
    playcount = item.get("UserData", {}).get("PlayCount", 0)
    item_id = item.get("Id")

    # Download image
    img_url = f"{JELLYFIN_URL}/Items/{item_id}/Images/Primary"
    img_response = requests.get(img_url, headers=headers)
    if img_response.status_code == 200:
        cid = f"image{image_count}"
        img = MIMEImage(img_response.content)
        img.add_header("Content-ID", f"<{cid}>")
        msg.attach(img)
        html += f"""
        <div class="item">
            <img src="cid:{cid}" alt="{name}">
            <div>
                <strong>{i:02d}. {name}</strong><br>
                Plays: {playcount}
            </div>
        </div>
        """
        image_count += 1
    else:
        # No image
        html += f"""
        <div class="item">
            <div>
                <strong>{i:02d}. {name}</strong><br>
                Plays: {playcount}
            </div>
        </div>
        """

html += "</body></html>"
alt_part.attach(MIMEText(html, "html"))

# Send email
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(EMAIL, APP_PASSWORD)
server.send_message(msg)
server.quit()
