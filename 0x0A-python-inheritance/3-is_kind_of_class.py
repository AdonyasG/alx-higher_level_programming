#!/usr/bin/python3
"""
Module - 3-is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    return true if obj is an instance or
    if obj is an instance inherited class
    else false
    """
    return isinstance(obj, a_class)
