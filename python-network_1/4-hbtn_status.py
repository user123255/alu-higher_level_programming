#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status and displays the response body
with its type and content.
"""

import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    try:
        response = requests.get(url)
        content = response.text
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
    except requests.exceptions.RequestException:
        print("Failed to fetch the status.")
