#!/usr/bin/python3
"""visbvuidfnvds"""

import json
import os


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    """jvnsduifvuisdnkvsd"""
    filename = "add_item.json"
    if os.path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []
    save_to_json_file(my_list, filename)
