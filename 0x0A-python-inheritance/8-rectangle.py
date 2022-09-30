#!/usr/bin/python3
"""
Module 8-rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle():
    """class Rectangle that inherits from base geometery"""
    def __init__(self, width, height):
        """initializtion and validation"""
        super. integer_validator("width", width)
        self.__width = width
        self. integer_validator("height", height)
        self.__height = height
