#!/usr/bin/python3
"""Script that fetches the X-Request-Id from the response header of a URL."""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
