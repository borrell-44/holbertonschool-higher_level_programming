#!/usr/bin/python3
"""Diplays you GitHub id"""


if __name__ == "__main__":
    import requests
    import sys

    x = requests.get('https://api.github.com/search/repositories?q=github+api', auth=(sys.argv[1], sys.argv[2]))
    print(x.json().get("id"))
