#!/usr/bin/python3
"""ijgfbvuidfbufdn"""


def add_attr(obj, attr_name, attr_value):
    """ojsdfviudsfidfs"""
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
