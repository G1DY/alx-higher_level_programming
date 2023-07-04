#!/usr/bin/python3
"""lists 10 commits (from the most recent to oldest)
   of the repository “rails” by the user “rails”
"""
import requests
import sys


def github_commits():
    url = "https://api.github.com/repos/{}/{}/commits/".format(
        sys.argv[2], sys.argv[1])
    response = requests.get(url)
    commits = response.json()
    if response.ok:
        for commit in commits[:10]:
            SHA = commit.get("sha")
            Author_Name = commit.get("commit").get("author").get("name")
            print("{}: {}".format(SHA, Author_Name))
    else:
        print("Could not fetch commits")


if __name__ == "__main__":
    github_commits()
