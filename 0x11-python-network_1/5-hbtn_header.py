#!/usr/bin/python3
"""Fetches a URL with pythons requests
library"""

if __name__ == "__main__":
    import requests
    import sys

    x = requests.get(sys.argv[1])
    list = x.__dict__.get("headers")
    if "X-Request-Id" in list:
        print(list.get("X-Request-Id"))
