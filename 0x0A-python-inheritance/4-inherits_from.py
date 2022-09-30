#!/usr/bin/python3
"""
Module - 4-inherits_from
"""


def inherits_from(obj, a_class):
    """
    return true if obj is an instance or
    if obj is an instance inherited class or subclass
    else false
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
