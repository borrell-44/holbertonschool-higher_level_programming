#!/usr/bin/python3
# Fetches a URL with pythons requests library

if __name__ == "__main__":
    import requests
    import sys

    x = requests.get('https://intranet.hbtn.io/status')
    print(x.__dict__["headers"]["X-Request-Id"])
