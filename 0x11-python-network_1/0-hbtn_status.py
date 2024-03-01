#!/usr/bin/python3
""" Python script that fetches `https://alx-intranet.hbtn.io/status`."""
from urllib.request import Request, urlopen


def fetch_url_content(url):
    """Fetch the contents of the provided url"""
    try:
        req = Request(url)
        with urlopen(req) as response:
            return response.read()
    except Exception as e:
        print(f'Error fetching content, {e}')
        return None


if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"
    content = fetch_url_content(url)
    if content:
        print('Body response:')
        print(f'\t- type: {type(content)}')
        print(f'\t- content: {content}')
        print(f'\t- utf8 content: {content.decode("utf-8")}')
