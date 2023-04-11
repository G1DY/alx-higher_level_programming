#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represents Rectangle using basegeometry"""
    def __init__(self, width, height):
        """initializes a rectangle

        Args:
            width: width of the rectangle
            height: length of the rectangle

        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
