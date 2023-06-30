#!/usr/bin/python3
"""This script fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.htbn.io/status') as url:
        body = url.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf8')}")
