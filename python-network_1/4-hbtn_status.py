#!/usr/bin/env python3
import requests

def main():
    url = "https://alu-intranet.hbtn.io/status"
    headers = {
        "User-Agent": "Mozilla/5.0"  # Spoof a simple browser user-agent
    }

    response = requests.get(url, headers=headers)
    body = response.text

    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")

if __name__ == "__main__":
    main()
