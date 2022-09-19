#!/usr/bin/python3
"""
Module 1-rectangle
Defines class rectangle
"""


class Rectangle:
    """
    class Square definition

    Args:
        width : width of a rectangle
        height: height of a rectangle

    Functions:
        __init__(self, width=0, height=0)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
    """
    def __init__(self, width=0, height=0):
        """initialize a rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter

        Return: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter

        Args:
            set width to value
        """
        if not (isinstance(value, (int))):
            raise TypeError(f"width must be an integer")
        if (isinstance(value, (int)) and value < 0):
            raise ValueError(f"width must be >= 0")
        self.__size = value

    @property
    def height(self):
        """
        Getter

        Return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter

        Args:
            sets height to value
        """
        if not (isinstance(value, (int))):
            raise TypeError(f"height must be an integer")
        if (isinstance(value, (int)) and value < 0):
            raise ValueError(f"height must be >= 0")
        self.__size = height
