#!/usr/bin/python3
"""a function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attr, value):
    """adds a new attribute if possible

    Args:
        obj: object to add an attribute
        attr: attribute to be added
        value: value of the attribute

    Raises:
        TypeError if attribute cant be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
