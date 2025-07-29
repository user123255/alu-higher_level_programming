#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status and displays the response body content."""

from urllib import request


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    with request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
