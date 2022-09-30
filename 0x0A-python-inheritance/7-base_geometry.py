#!/usr/bin/python3
"""
Module 7-base_geometry
"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """area not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates if its integer"""
        if type(value) is not int:
            raise TypeError(f"{name:s} must be an integer")
        if value <= 0:
            raise ValueError(f"{name:s} must be greater than 0")
