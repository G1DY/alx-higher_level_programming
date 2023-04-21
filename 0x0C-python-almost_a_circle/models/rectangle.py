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
        super().__init__(id)

        @property
        def width(self):
            """get the width of the rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            """sets the width value

            Args:
                value: value of width in int

            Raises:
                TypeError: if value is non-int
                ValueError: if value is <=0
            """
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """gets the height of the rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            """sets the height value

            Args:
                value : value of height must be an int

            Raises:
                TypeError: if value is not an int
                ValueError: if value <= 0
            """
            if type(value) != int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """gets the x coordinate"""
            return self.__x

        @x.setter
        def x(self, value):
            """sets the x-coordinate to position

            Args:
                x: value of x coordinate as an int

            Raises:
                TypeError: if x is not an int
                ValueError: if x is < 0
            """
            if type(value) != int:
                raise TypeError("x must be an integer")
            if x < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            """gets the y coordinate"""
            return self.__y

        @y.setter
        def y(self, value):
            """sets the y coordinate to position

            Args:
                y: value of y coordinate as an int

            Raises:
                TypeError: y must be an integer
                ValueError: y must be > 0
            """
            if type(value) != int:
                raise TypeError("y must be an integer")
            if y < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
