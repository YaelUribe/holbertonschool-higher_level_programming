#!/usr/bin/python3
"""Script to fetch an URL and displaying the value of given variable"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen("{}".format(sys.argv[1])) as response:
        html = response.read()
        for key in response.__dict__:
            value = response.headers.get('X-Request-Id')
        print(value)
