#!/usr/bin/python3
"""
Module - 12-pascal triangle
"""


def pascal_triangle(n):
    """ Returns list in pascal triangle"""
    listt = []
    for i in range(n):
        listt.append([])
        for j in range(i + 1):
            if j == 0 or j == 1:
                listt[i].append(1)
            else:
                listt[i].append(listt[i - 1][j - 1] + listt[i - 1][j])
        return listt
