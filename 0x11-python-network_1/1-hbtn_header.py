#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header
"""
from urllib.request import Request, urlopen
from sys import argv


def get_url_response(url):
    """Return response obj from the provided url"""
    try:
        req = Request(url)
        with urlopen(req) as response:
            return response
    except Exception as e:
        print(f'Error fetching content, {e}')
        return None


if __name__ == '__main__':
    url = argv[1]
    response = get_url_response(url)
    if response:
        print(response.headers.get('X-Request-Id'))
