#!/usr/bin/python3
"""Python script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally displays the body
of the response.
"""
import requests
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    email = argv[2]
    data = {'email': email}
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
