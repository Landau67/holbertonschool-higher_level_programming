#!/usr/bin/python3
"""eringiuegnf"""

import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        raise(f"Error code :{e.code}")
