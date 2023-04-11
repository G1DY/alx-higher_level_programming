#!/usr/bin/python3
"""a class Square that inherits from Rectangle (9-rectangle.py)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines a square"""

    def __init__(self, size):
        """initialize a new square
        Args:
            size: width of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
