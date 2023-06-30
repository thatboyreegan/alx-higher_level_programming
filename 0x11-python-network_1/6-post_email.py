#!/usr/bin/python3
"""This script takes in a URL and an email, sends a POST request
with the email as the paramter and displys the response"""

import sys
import requests

if __name__ == '__main__':
    email = {"email": sys.argv[2]}
    response = requests.post(sys.argv[1], data=email)
    print(response.text)
