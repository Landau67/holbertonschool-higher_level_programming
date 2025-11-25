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
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """jofdshufbifbifs"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
