#!/usr/bin/python3
"""a function that writes a string to a text file (UTF8)
   and returns the number of characters written
"""


def write_file(filename="", text=""):
    """Returns the number of lines in a text file"""
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1
    return lines
