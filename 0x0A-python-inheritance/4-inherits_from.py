#!/usr/bin/python3
"""a function that returns True if the object is an instance of
   a class that inherited (directly or indirectly) from
   the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """checks if an object is an instance of a class inherited from

    Args:
        obj: object to check
        a_class: class to compare from

    Returns:
        True if the class is the one the object inherited
        False otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
