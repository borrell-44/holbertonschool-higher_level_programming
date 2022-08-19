#!/usr/bin/python3
"""Fetches a URL with pythons requests library"""

if __name__ == "__main__":
    import requests

    x = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print(f"\t- type: {type(x.text)}")
    print(f"\t- content: {x.text}")
