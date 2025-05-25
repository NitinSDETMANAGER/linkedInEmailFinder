"""
Author: Nitin Choudhary
Description: Fetches email address from a LinkedIn profile using Apollo API.
"""

import requests

# Paste your real API key here
API_KEY = "PASTE_YOUR_API_KEY_HERE"

def get_email_from_linkedin(linkedin_url):
    api_url = "https://api.apollo.io/v1/people/match"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "x-api-key": API_KEY,
    }

    payload = {
        "linkedin_url": linkedin_url,
        "reveal_personal_emails": True
    }

    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        person = data.get("person", {})
        email = person.get("email")

        if email:
            return f"✅ Email found: {email}"
        else:
            return "❌ No email found for this person."

    if response.status_code == 401:
        return f"🔑 Check your API key → {response.status_code}: {response.text}"
    else:
        return f"[ERROR] Apollo API failed → {response.status_code}: {response.text}"

# Example usage
if __name__ == "__main__":
    linkedin = input("🔗 Enter LinkedIn URL: ")
    print(get_email_from_linkedin(linkedin))
