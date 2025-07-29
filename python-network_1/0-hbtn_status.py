#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status and displays the response body."""

from urllib import request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    headers = {"User-Agent": "Mozilla/5.0"}  # Set a browser-like User-Agent
    req = request.Request(url, headers=headers)

    with request.urlopen(req) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
