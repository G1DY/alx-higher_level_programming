#!/usr/bin/python3
"""a function that returns True if the object is an instance
   of a class that inherited (directly or indirectly) from
   the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """checks if an object is an instance of an inherited instance class

    Args:
        obj: object instance to check
        a_class: class instance to match

    Returns:
        True if object instance is an inherited instance of a class
        otherwise False
    """
    if isinstance(obj, a_class):
        return True
    return False
