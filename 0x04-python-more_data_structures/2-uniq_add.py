#!/usr/bin/python3
def uniq_add(my_list=[]):
    x = 1
    for i in my_list:
        if my_list[i] != i:
            x = x + i
    return x
