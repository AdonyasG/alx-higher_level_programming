#!/usr/bin/python3
"""
Module 11-square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size):
        """create square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """return, the square description: [Square] <width>/<height>"""
        return f"[Square] {self.__size:d}/{self.__size:d}"
