#!/usr/bin/python3
"""
Sends a POST request to search_user endpoint with letter parameter.

Usage:
    ./8-json_api.py [letter]
"""

import sys
import requests


if __name__ == "__main__":
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}

    try:
        response = requests.post(url, data=data)
        response_json = response.json()

        if response_json:
            print("[{}] {}".format(
                response_json.get('id'),
                response_json.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
