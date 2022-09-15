#!/usr/bin/python3
"""
    Module 0-add_integer
    Returns:
        sum of two integers
"""


def add_integer(a, b=98):
    """
    Adds two integers
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    try:
        return a + b
    except TypeError:
        if not (isinstance(b, (int))):
            raise TypeError("b must be an integer")
        else:
            raise TypeError("a must be an integer")
