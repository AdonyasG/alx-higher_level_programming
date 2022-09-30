#!/usr/bin/python3
"""
Module 9-rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle():
    """class Rectangle that inherits from base geometery"""
    def __init__(self, width, height):
        """initializtion and validation"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """return area"""
        return self.__width * self.__height

    def __str__(self):
        """prints [Rectangle] <width>/<height>"""
        return f"[Rectangle] {self.__width:d}/{self.__height:d}"
