#!/usr/bin/python3
"""jnefgbjfgbd"""


def class_to_json(obj):
    result = []
    for key, value in obj.__dict.__items():
        if isinstance(value, list, dict, str, int, bool):
            result[key] = value
    return result
