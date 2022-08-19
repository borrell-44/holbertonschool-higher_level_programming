#!/usr/bin/python3
# Fetches an URL and prints the response body

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        body = response.read()
        print(body)
