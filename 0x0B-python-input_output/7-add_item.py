#!/usr/bin/python3
"""
Module 9-add_item
Contains function that adds and saves to Python obj to JSON file; loads objects
"""


import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    i = load_from_json_file(filename)
except FileNotFoundError:
    i = []

save_to_json_file(i + sys.argv[1:], filename)
