#!/usr/bin/python3
"""
Module 9-student
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

    def to_json(self):
        """
        Returns dictionary description with simple data structure
        """
        self.__dict__
