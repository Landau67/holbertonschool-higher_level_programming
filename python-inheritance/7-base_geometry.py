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
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
