#!/usr/bin/python3
"""Takes GitHub credentials (username and password)
   and uses the GitHub API to display id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


def display_id():
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))


if __name__ == "__main__":
    display_id()
