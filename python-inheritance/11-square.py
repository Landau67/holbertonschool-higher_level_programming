#!/usr/bin/python3
"""ijfvbfgbvuf"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """jofdshufbifbifs"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        print(f"[Rectangle] {self.__size}/{self.__size}")

    def area(self):
        return self.__size ** 2
