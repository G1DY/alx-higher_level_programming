#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
   package requests
"""
import requests


def requests():
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))


if __name__ == "__main__":
    requests()
