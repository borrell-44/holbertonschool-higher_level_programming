#!/usr/bin/python3
"""Fetches a URL with pythons requests library"""

if __name__ == "__main__":
    import requests
    import sys

    x = requests.get(sys.argv[1])
    if x.status_code >= 400:
        print("Error code: {}".format(x.status_code))
    else:
        print(x.text)
