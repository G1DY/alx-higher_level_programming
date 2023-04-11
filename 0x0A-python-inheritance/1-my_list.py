#!/usr/bin/python3
"""a class that inherits from the list"""


class MyList(list):
    """impliments print function for the class list"""
    def print_sorted(self):
        print(sorted(self))
