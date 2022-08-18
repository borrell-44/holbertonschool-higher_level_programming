#!/usr/bin/bash
# Sends a request to the given URL and prints the size of the body response
curl -s "$1" | wc -c
