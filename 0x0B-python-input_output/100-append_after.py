#!/usr/bin/python3
"""
Module 100-append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """appends str after lines that include keyword (search_string)"""
    with open(filename, mode="r+", encoding="utf-8") as f:
        a = ""
        for i in f:
            a += i
            if search_string in i:
                a += new_string
        f.seek(0)
        f.write(a)
