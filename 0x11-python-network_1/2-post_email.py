#!/usr/bin/python3
"""Script to take in an URL and send a POST request"""
import sys
from urllib import parse, request

if __name__ == "__main__":
    email = sys.argv[2]
    content = parse.urlencode({'email': email})
    content = content.encode('ascii')
    with request.urlopen(sys.argv[1], content) as response:
        html = response.read().decode('utf-8')
    print(html)
