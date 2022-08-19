#!/usr/bin/python3
"""Fetches a URL with pythons requests library"""

if __name__ == "__main__":
    import requests
    import sys

    letter = dict(q="")
    if len(sys.argv) >= 2:
        letter = dict(q=sys.argv[1])

    x = requests.post("http://0.0.0.0:5000/search_user", data=letter)
    try:
        response = x.json()
        if not response:
            print("No result")
        else:
            print("[{}] {}".format(response.get('id'), response.get('name')))
    except:
        print("Not a valid JSON")
