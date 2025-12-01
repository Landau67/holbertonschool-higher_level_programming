#!/usr/bin/python3
"""kvndfobioefngbf"""

import urllib.request


if __name__ == "__main__":
    with urllib.request.Request('https://intranet.hbtn.io/status') as response:
        body = response.read()
print("Body response:")
print(f"    - type: {type(body)}")
print(f"    - content: {body}")
print(f"    - utf8 content: {body.decode('utf-8')}")
