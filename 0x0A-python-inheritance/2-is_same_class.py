#!/usr/bin/python3
"""a function that returns True if the object is exactly
   an instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """checks if an object is an instance of a class

    Args:
        obj: object to check
        a_class: class to compare and match

    Returns: 
        True if object is in class otherwise False
    """
    if type(obj) == a_class:
        return True
    return False
