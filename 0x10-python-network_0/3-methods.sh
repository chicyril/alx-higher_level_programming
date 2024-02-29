#!/bin/bash
# Displays all HTTP methods the server will accept.
curl -sI -X OPTIONS "$1" | awk -F': ' '/Allow/ {print $2}'
