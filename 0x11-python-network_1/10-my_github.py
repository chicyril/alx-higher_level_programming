#!/usr/bin/python3
""" Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(argv[1], argv[2])
    try:
        response = requests.get("https://api.github.com/user", auth=auth)
        print(response.json().get("id"))
    except Exception as e:
        print('Error:', e)
