#!/usr/bin/python3
"""kvndfobioefngbf"""

import urllib.request


if __name__ == "__main__":
    with urllib.request.Request('https://intranet.hbtn.io/status') as response:
        body = response.read()
