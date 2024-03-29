#!/usr/bin/python3
"""lists 10 commits (from the most recent to oldest)
   of the repository “rails” by the user “rails”
"""
import requests
import sys


def gbcommits():
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    response = requests.get(url)
    commits = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i]["sha"],
                commits[i]["commit"]["author"]["name"]
             ))
    except IndexError:
        pass


if __name__ == "__main__":
    gbcommits()
