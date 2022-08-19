#!/usr/bin/python3
# Fetches a URL with pythons requests library

if __name__ == "__main__":
    import requests
    import sys

    data = dict(email=sys.argv[2])
    x = requests.post(sys.argv[1], data=data)
    print(x.text)
