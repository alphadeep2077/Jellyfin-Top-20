# To find your Library id , use this scipt !!

import requests

#  Replace these with your actual Jellyfin server details
JELLYFIN_URL = "http://Your URL:8096"
API_KEY = "Your-API-KEY"

# Construct API request
url = f"{JELLYFIN_URL}/Library/MediaFolders"
headers = {
    "X-Emby-Token": API_KEY
}

# Make the request
response = requests.get(url, headers=headers)

# Output
print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    print("\nYour Libraries:\n")
    for item in data.get("Items", []):
        print(f"Name: {item['Name']}  -->  ID: {item['Id']}")
else:
    print("Failed to fetch libraries.")
    print("Response:", response.text)
