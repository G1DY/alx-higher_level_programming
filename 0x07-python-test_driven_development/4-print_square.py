#!/usr/bin/python3
"""defines a function that prints square with #"""


def print_square(size):
    """prints a square with #

    Args:
        size: width of the square an integer

    Raises:
        TypeError: if size is not an int
        ValueError: if size is < 0

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end = "") for j in range(size)]
        print("")
    
