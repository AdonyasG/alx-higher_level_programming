#!/usr/bin/python3
"""
Module 10-student
Contains class Student
"""


class Student():
    """
    Public Attributes:
        first_name
        last_name
        age
    Public Methods:
        to_json
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary description with simple data structure

        Returns:
            returns passed attr or
            returns entire dic if no attrs are passed
        """
        if attrs is None:
            return self.__dict__
        else:
            a = {}
            for i in attrs:
                if i in self.__dict__.keys()
                a[i] = self.__dict__[i]
            return a
