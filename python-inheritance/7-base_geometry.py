#!/usr/bin/python3
"""ijfvbfgbvuf"""


class BaseGeometry:
    """vejofvfvnfnj"""

    def area(self):
        """jnfgiugfdgfdg"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """njfgdjjsdnfigdsfhfv"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
