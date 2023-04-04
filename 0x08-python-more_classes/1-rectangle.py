#!/usr/bin/python3
"""a class that defines a rectangle"""


class Rectangle:
    """represents a rectangle"""

    def __init__(self, width = 0, height = 0):
        """initialize the class rectangle
        Args:
            width = the width of the rectangle
            height = the height/length of the rectangle

        Raises:
            TypeError: if not an integer
            ValueError: if less than 0
        """
        self.width = width
        self.heght = height

    @property
    def width(self):
        """retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    """
    def area(self):
        """return the area of the rectangle"""
        return(self.__width * self.__height)

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width + self.__height) * 2))
    """
