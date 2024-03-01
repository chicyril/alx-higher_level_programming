#!/usr/bin/python3
"""Python script that fetches `https://alx-intranet.hbtn.io/status` using the
python request package.
"""
import requests


if __name__ == '__main__':
    response = requests.get('https://alx-intranet.hbtn.io/status')
    try:
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
    print('Body response:')
    print(f'\t- type: {type(response.text)}')
    print(f'\t- content: {response.text}')
