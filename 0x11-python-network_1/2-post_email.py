#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response (decoded in utf-8)
"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv


def fetch_url_content(url, data=None):
    """Fetch the contents of the provided url"""
    try:
        req = Request(url, data)
        with urlopen(req) as response:
            return response.read()
    except Exception as e:
        print(f'Error fetching content, {e}')
        return None


if __name__ == '__main__':
    url = argv[1]
    params = {'email': argv[2]}
    data = urlencode(params).encode('utf-8')
    content = fetch_url_content(url, data)
    if content:
        print(content.decode('utf-8'))
