#!/usr/bin/python3
# Fetches a URL with pythons requests library

if __name__ == "__main__":
    import requests
    import sys

    x = requests.get(sys.argv[1])
    print(x.__dict__.get("headers")["X-Request-Id"])
