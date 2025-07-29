#!/usr/bin/python3
"""
Fetches the status from http://0.0.0.0:5050/status
and prints the body of the response.
"""

import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"
    response = requests.get(url)
    body = response.text

    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
