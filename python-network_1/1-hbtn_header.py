#!/usr/bin/python3
"""jbndfinbdfmnbd"""

import urllib.request
import sys


if __name__ == "__main__":
    url = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        result = headers.get('X-Request-Id')
        print(result)
