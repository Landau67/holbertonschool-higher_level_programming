#!/usr/bin/python3
"""ijfvbfgbvuf"""


class BaseGeometry:
    """vejofvfvnfnj"""
    pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("def integer_validator(self, name, value):")
        if value <= 0:
            raise ValueError("def integer_validator(self, name, value):")
