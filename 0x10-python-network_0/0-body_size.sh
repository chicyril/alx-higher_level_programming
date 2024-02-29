#!/bin/bash
# Write a Bash script that prints the content length of a http response.
echo "$(curl -sI "$1" | grep -i '^content-length:' | awk '{print $2}')"
