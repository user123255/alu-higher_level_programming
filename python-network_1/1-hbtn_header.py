#!/usr/bin/python3
"""Fetches a URL and displays the value of X-Request-Id 
from the response header"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.info()
        print(headers.get("X-Request-Id"))
