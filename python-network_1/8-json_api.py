#!/usr/bin/python3
"""gshfhdfxg"""

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    data = {"q": letter}
    response = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        json_response = response.json()
        if not json_response:
            print("No result")
        else:
            name = json_response.get('name')
            id = json_response.get('id')
            print(f"[{id}] {name}")
    except Exception as e:
        print("Not a valid JSON")
