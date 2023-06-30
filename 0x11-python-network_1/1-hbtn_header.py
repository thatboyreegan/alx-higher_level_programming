#!/usr/bin/python3
"""This script takes a URL and sends a request so as to display the value
of X-Request-Id"""

import urllib.request
import sys

if __name__ == "__main__":
    ulr = sys.argv[1]
    with urllib.request.urlopen(ulr) as response:
        tmp = response.getheader('X-Request-Id')
        print(tmp)
