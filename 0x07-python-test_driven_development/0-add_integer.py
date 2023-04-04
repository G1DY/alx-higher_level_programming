#!/usr/bin/python3
"""defines integer  addition module"""


def add_integer(a, b=98):
    """returns the integer addition of a and b

    Agrs:
        a: first number
        b:second number

    Raises:
        TypeError: if a and b are not integers or floats
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
