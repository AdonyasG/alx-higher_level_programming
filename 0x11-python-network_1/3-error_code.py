#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in the
header of the response.
"""

import urllib.request
from urllib.error import HTTPError, URLError
import sys

if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('utf-8'))
    except Exception as e:
        print("Error code: {}".format(e.code))
