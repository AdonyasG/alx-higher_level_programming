#!/usr/bin/python3
"""script that fetches a url using the urlib script"""

import urllib.request

if __name__ == '__main__':
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(page)))
        print('\t- content: {}'.format(page))
        print('\t- utf8 content: {}'.format(page.decode('UTF-8')))