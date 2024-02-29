#!/bin/bash
# Print the body of a http 200 OK response.
curl -s -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"
