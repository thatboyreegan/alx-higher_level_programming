#!/usr/bin/python3
"""This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""


import requests
import sys

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]

    tmp_dict = {"q": letter}
    try:
        response = requests.post("http://0.0.0.0:5000/search_user",
                                 data=tmp_dict)
        reprs = response.json()
        if reprs == {}:
            print("No result")
        else:
            print(f"[{reprs.get('id')}] {reprs.get('name')}")
    except ValueError:
        print("Not a valid JSON")
