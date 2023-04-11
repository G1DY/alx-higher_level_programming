#!/usr/bin/python3
"""a class MyInt that inherits from int"""


class MyInt(int):
    """inverts int operators == and !="""

    def __eq__(self, value):
        """replace == with !="""
        return self.real != value

    def __ne__(self, value):
        """replace != with =="""
        return self.real == value
