import requests
import random
import re

# Facebook's user ID pattern
pattern = r"[0-9]{1,15}"

def get_random_facebook_id():
    # Generate a random Facebook ID
    facebook_id = str(random.randint(100000000, 999999999999))
    return facebook_id

def check_facebook_id(facebook_id):
    # Send a request to Facebook's mobile website to check if the ID exists
    url = f"https://m.facebook.com/{facebook_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Android SDK built for x86_64)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # If the ID exists, extract the user's name
        name_pattern = r"<title>(.*?)</title>"
        name_match = re.search(name_pattern, response.text)
        if name_match:
            name = name_match.group(1)
            return facebook_id, name
    return None, None

def clone_facebook_ids():
    while True:
        facebook_id = get_random_facebook_id()
        print(f"Checking ID: {facebook_id}...")
        id, name = check_facebook_id(facebook_id)
        if id:
            print(f"Found ID: {id} - {name}")
        else:
            print(f"ID not found: {facebook_id}")

if __name__ == "__main__":
    clone_facebook_ids()