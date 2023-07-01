#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""
import sys
import urllib.request


def request_urlopen():
    url = sys.argv[1]
    request = urlib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))


if __name__ == "__main__":
    request_urlopen()
