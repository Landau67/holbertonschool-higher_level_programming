#!/usr/bin/python3
"""ijfvbfgbvuf"""


class BaseGeometry:
    """vejofvfvnfnj"""

    def area(self):
        """jnfgiugfdgfdg"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """njfgdjjsdnfigdsfhfv"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
