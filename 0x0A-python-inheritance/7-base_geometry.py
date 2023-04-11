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

    def integer_validator(self, name, value):
        """validates value

           Args:
               name: a string
               value: value to validate
           Raises:
               TypeError if value is not an integer
               ValueError if value <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
