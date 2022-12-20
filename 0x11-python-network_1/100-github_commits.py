#!/usr/bin/python3
"""
Please list
10 commits (from the most recent to oldest) of the repository
"""

import requests
import sys

if __name__ == '__main__':
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    r = requests.get(url)
    res = r.json()
    for i in res[:10]:
        print("{}: {}".format(i.get("sha"), i['commit']['author']['name'],))
