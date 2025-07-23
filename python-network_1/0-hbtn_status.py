#!/usr/bin/python3
"""Fetches a URL and displays formatted response using urllib"""

import urllib.request

url = "http://0.0.0.0:5050/status"  # updated from https://alu-intranet.hbtn.io/status

with urllib.request.urlopen(url) as response:
    body = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))
