#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status and displays the body response"""

import urllib.request

url = "http://0.0.0.0:5050/status"  # Change this to https://intranet.hbtn.io/status for final submit

with urllib.request.urlopen(url) as response:
    body = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
