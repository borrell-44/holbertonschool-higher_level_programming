#!/usr/bin/python3
# Sends a POST request to the given URL with the email as a parameter

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    data = urllib.parse.urlencode({"email": "hr@holbertonschool.com"})
    with urllib.request.urlopen(sys.argv[1], data=data) as response:
        body = response.read().decode('utf-8')
        print(body)
