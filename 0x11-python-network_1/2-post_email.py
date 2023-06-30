#!/usr/bin/python3
"""This script takes a URL and an email, sends a POST request
with the email as the paramter and displys the response"""

import sys
from urllib import request, parse

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = parse.urlencode({'email': email}).encode('ascii')
    with request.urlopen(url, data) as response:
        tmp = response.read()
        print(tmp.decode('utf-8'))
