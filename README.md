#  Jellyfin Top Played Music Email Report 

This Python script fetches the **Top 20 most played items** (music albums/tracks) from your Jellyfin library and sends a  email  to your Gmail with:


- Title of each track or album
- Play counts
- Thumbnails (embedded if available)

---

##  Features

- Uses Jellyfin API to fetch play counts and images
- Sends results directly to Gmail using SMTP
- Images are embedded via CID (Content-ID)
- Clean, simple HTML (no styling or CSS)

---

##  Requirements

- Python 3.7+
- A running Jellyfin server with API access
- Gmail account with **App Passwords** enabled
- Python package:
  - `requests`

---

Install with:

```bash
pip install requests
```

---

# Configuration

Edit the script to include your credentials and IDs:

```
JELLYFIN_URL = "http://<your-jellyfin-ip>:8096"
API_KEY = "<your_jellyfin_api_key>"
USER_ID = "<your_jellyfin_user_id>"
LIBRARY_ID = "<your_music_library_id>"

EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_gmail_app_password"
```

You can get the IDs from the Jellyfin API or inspect browser network requests or you can run my script : jellyfin-library_id.py to get your library .

---

# How to Run 

```
python jellyfin_email_report.py
```
It will send an email to your Gmail with:

- Top 20 most played items

- Play counts

- Images (if available)

---
# Security 

Use a .env file or environment variables in production.

---

# License

MIT License

Created by Deep Doshi

Inspired by Jellyfin , built with Python . 

