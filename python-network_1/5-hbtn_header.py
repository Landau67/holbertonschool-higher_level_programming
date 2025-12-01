#!/usr/bin/python3
"""mkrkmgkmgefvbjijefg"""


import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    result = response.headers.get('X-Request-Id')
    print(result)
