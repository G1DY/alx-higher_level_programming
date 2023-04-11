#!/usr/bin/python3
"""defines a class BaseGeometry"""


class BaseGeometry:
    """represents a BaseGeometry

       Raises:
           Exception area is not implemented
    """

    def area(self):
        """not implemented"""
        raise Exception("area() is not implemented")
