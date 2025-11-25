#!/usr/bin/python3
"""ijfvbfgbvuf"""

BaseGeometry = __import__('8-rectangle').BaseGeometry


class Rectangle(BaseGeometry):
    """jofdshufbifbifs"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        print(f"[Rectangle] {self.__width}/{self.__height}")

    def area(self):
        return self.__width * self.__height
