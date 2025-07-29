#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status using urllib."""

from urllib import request


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    with request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
