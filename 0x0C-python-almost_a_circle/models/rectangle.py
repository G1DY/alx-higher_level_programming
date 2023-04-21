#!/usr/bin/python3
"""Defines a class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Represents class rectangle from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize a rectangle

        Args:
            width: width of the rectangle in int
            height: height of the rectangle in int
            x: x coordinate in int
            y: y coordinate in int
            id: identity of the new rectangle in int

        Raises:
            TypeError: if either the width or height is not an int
            ValueError: if either the width or height <= 0
            TypeError: if either x or y is not an int
            ValueError: if either x or y < 0
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init(id)

        @property
        def width(self):
            """get the width of the rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            """sets the width value"""
            self.__width = value

        @property
        def height(self, value):
            """gets the height of the rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            """sets the height value"""
            self.__height = value
