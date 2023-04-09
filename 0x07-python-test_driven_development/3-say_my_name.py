#!/usr/bin/python3
"""defines a function print names"""


def say_my_name(first_name, last_name=""):
    """prints names

    Args:
        first_name: string of first name
        last_name: string of second name

    Raises:
        TypeError: if first name or last name is not a string

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
