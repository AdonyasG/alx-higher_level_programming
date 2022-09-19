#!/usr/bin/python3
"""
Module 7-rectangle
Defines class rectangle
str representation
public attribute that keeps track of number of insatnces
public attribute for symbol sting representation
static method
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
        area(self)
        perimeter(self)
        __str__(self)
        __repr__(self)
        __del__(self)
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize a rectangle"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        self.__width = value

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
        self.__height = value

    def area(self):
        """
        calculate Area of rectangle

        Returns: Area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        calculates perimeter of a rectangle

        Returns: perimeter
        """
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """ Prints rectangle with #'s """
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = "\n".join([str(self.print_symbol) * self.__width
                        for rows in range(self.__height)])
        return rec

    def __repr__(self):
        """string representaion to create new instance"""
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """del was called"""
        print('Bye rectangle...')
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
