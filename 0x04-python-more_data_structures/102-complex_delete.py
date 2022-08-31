#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, values in a_dictionary:
        if values == value:
            del a_dictionary[key]
    return a_dictionary
