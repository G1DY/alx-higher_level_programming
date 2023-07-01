#!/usr/bin/python3
"""sends a request to the URL and displays the body
   of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.error


def request_urlopen():
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    request_urlopen()
