#!/usr/bin/python3
"""
Module 6-square
Defines class Square with private size and position
prints "#" to stdout
"""


class Square:
    """
    class Square definition

    Args:
        size : size of a side in square

    Functions:
        __init__(self, size)
                size(self)
        size(self, value)
        position(self)
        position(self, value)
        area(self)
        my_print(self)
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes square

        Attributes:
            size: size of a side of square
            position : tuple of two positive integers
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter

        Return: size
        """
        return self.__size

    @size.setter
    def size(self, val):
        """
        Setter

        Args:
            val: set size to val
        """
        if not (isinstance(val, (int))):
            raise TypeError(f"size must be an integer")
        if (isinstance(val, (int)) and val < 0):
            raise ValueError(f"size must be >= 0")
        self.__size = val

    @property
    def position(self):
        """"
        Getter
        Return: position
        """
        return self.__position

    @position.setter
    def position(self, val):
        """
        Setter

        Args:
            value: sets position to tuple if value is tuple of 2 positive ints
        """
        if type(val) is not tuple or len(val) != 2 or \
           type(val[0]) is not int or type(val[1]) is not int or \
           val[0] < 0 or val[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = val

    def area(self):
        """
        Calculates area of square

        Returns:
            area
        """
        area = (self.__size)**2
        return area

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] +
                             "#" * self.__size
                             for rows in range(self.__size)]))

    def __str__(self):
        """
        String representation of square so call to print works
        Example: print(my_square)
        """
        string = ""
        if self.__size == 0:
            return string

        string += "\n" * self.position[1]
        string += "\n".join([" " * self.__position[0] +
                             "#" * self.__size
                             for rows in range(self.__size)])
        return string
