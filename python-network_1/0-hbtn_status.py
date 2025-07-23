#!/usr/bin/python3
"""Fetches http://0.0.0.0:5050/status using urllib and prints formatted response"""

import urllib.request


def fetch_status():
    """Fetch and display HTTP response body in specified format"""
    url = "http://0.0.0.0:5050/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))


if __name__ == "__main__":
    fetch_status()
