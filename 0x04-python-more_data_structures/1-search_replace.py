#!/usr/bin/python3
def search_replace(my_list, search, replace):
    x = my_list[:]
    for i in range(len(x)):
        if x[i] == search:
            x[i] = replace
    return x
#   to replace at a given index
#    for i in range(len(x)):
#        i = x.index(search)
#        x = x[:i]+[replace]+x[i+1:]
#    return x
