#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    i = [i for i in my_list]
    return [(x % 2 == 0) for x in i]
