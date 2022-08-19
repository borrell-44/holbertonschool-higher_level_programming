#!/usr/bin/python3
"""Sends a POST request to the given URL with the
email as a parameter"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    d = dict(email=sys.argv[2])
    f = urllib.parse.urlencode(d)
    f = f.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], f)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body)
