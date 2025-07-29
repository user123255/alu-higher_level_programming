#!/usr/bin/python3
"""Fetches the status from a fixed URL using the requests package."""

import requests


if __name__ == "__main__":
    try:
        response = requests.get("http://0.0.0.0:5050/status")
        content = response.text
    except Exception:
        response = requests.get("https://intranet.hbtn.io/status")
        content = response.text

    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
