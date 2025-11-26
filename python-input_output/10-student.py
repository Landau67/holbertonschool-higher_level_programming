#!/usr/bin/python3
"""fisduvudsnfv"""


class Student:
    """vsdvsdvsdvds"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            Result = []
            for i in attrs:
                if hasattr(self, i):
                    Result[i] = getattr(self, i)
        return Result
