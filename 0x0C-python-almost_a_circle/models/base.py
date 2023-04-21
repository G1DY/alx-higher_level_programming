#!/usr/bin/python3
"""Defines a the first class Base"""


class Base:
    """Represents “base” of all other classes in this project
       The goal of it is to manage id attribute in all the  future
       classes and to avoid duplicating the same code

    Attribute:
        __nb_objects = 0:number of base objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes the first base

        Args:
            id: an int representing id of new base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
