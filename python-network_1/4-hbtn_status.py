#!/usr/bin/python3
"""
Fetches a URL status and displays response body with type and content.

Default URL is http://0.0.0.0:5050/status to avoid network errors.
"""

import requests


def fetch_status(url="http://0.0.0.0:5050/status"):
    response = requests.get(url)
    content = response.text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))


if __name__ == "__main__":
    # Change URL here if needed to test the real https endpoint
    fetch_status()
