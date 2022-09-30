#!/usr/bin/python3
"""
Module 1-my_list
"""


class MyList(list):
    """inherits from list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
