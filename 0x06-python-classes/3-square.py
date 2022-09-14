#!/usr/bin/python3
"""
Module 3-square
Defines class Square
"""


class Square:
    """
    class Square definition

    Args:
        size : size of a side in square

    Functions:
        __init__(self, size)
        area(self)
    """
    def __init__(self, size=0):
        """
        Initializes square

        Attributes:
            size: size of a side of square
        """
        if not (isinstance(size, (int))):
            raise TypeError(f"size must be an integer")
        if (isinstance(size, (int)) and size < 0):
            raise ValueError(f"size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates area of square

        Returns:
            area
        """
        area = (self.__size)**2
        return area
