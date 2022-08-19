#!/usr/bin/python3
"""Sends an request for the given URL"""

if __name__ == "__main__":
    # Comment
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        body = response.__dict__['headers']
        print(body.get('X-Request-Id'))
