#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    i = [i for i in my_list]
    if idx < 0:
        return i
    elif idx > len(my_list):
        return i
    else:
        i[idx] = element
        return i
# alternate ways to copy list
# i = my_list[:]
# i = my_list.copy()
