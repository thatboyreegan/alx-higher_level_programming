#!/usr/bin/python3
"""This script  takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""


import requests
import sys


if __name__ == "__main__":
    t_auth = (sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=t_auth)
    print(response.json().get('id'))
