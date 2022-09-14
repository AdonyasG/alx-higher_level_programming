#!/usr/bin/python3
"""Define MagicClass"""
import math


class MagicClass:
    """initialize and define"""
    def __init__(self, radius=0):
        """init"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError(f"radius must be a number")
        self.__radius = radius

    def area(self):
        """calc area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """calc circumference"""
        return 2 * math.pi * self.__radius
