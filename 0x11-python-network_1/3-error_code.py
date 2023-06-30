#!/usr/bin/python3
"""This script takes a URL,sends a request and displays the response"""

import sys
from urllib import request, error

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            tmp = response.read()
            print(tmp.decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
