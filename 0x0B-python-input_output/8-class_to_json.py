#!/usr/bin/pytho3
"""
Module 10-class_to_json
class to json
"""


def class_to_json(obj):
    """Returns dictionary description with simple data structure
    Args:
        obj: python object
    """
    return obj.__dict__
