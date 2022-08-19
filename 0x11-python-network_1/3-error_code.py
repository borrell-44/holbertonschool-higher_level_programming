#!/usr/bin/python3
# Sends a request to the given URL and displays the response body

if __name__ == "__main__":
    # Comment
    import urllib.request
    import urllib.error
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        err_num = e.code
        print("Error code: {}".format(err_num))
