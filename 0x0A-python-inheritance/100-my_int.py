#!/usr/bin/python3
"""
Module 100-my_int
"""


class MyInt(int):
    """ class MyInt """
    def __init_(self, num):
        """init num"""
        self.num = num

    def __eq__(self, num):
        """if not equal"""
        return num != num

    def __ne__(self, num):
        """if equal"""
        return num == num
