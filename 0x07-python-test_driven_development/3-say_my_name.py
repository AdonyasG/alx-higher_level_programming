#!/usr/bin/python3
"""
This function prints my name
Returns:
My name
"""


def say_my_name(first_name, last_name=""):
    """prints a name to stdout
    Returns name
    """
    try:
        print(first_name + " " + last_name)
    except TypeError:
        if not (isinstance(first_name, str)):
            raise TypeError("first_name must be a string")
        else:
            raise TypeError("last_name must be a string")
