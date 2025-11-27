#!/usr/bin/python3

import csv

import json


def convert_csv_to_json(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            data_list = list(csv_reader)
        with open(filename, 'w', encoding="utf-8") as file:
            json.dump(data, filename)
        return True
    except FileNotFoundError:
        return False
