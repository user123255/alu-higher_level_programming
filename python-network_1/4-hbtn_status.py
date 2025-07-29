#!/usr/bin/python3
"""Fetches status from a given URL using the requests package."""

import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"
    response = requests.get(url)
    content = response.text

    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
