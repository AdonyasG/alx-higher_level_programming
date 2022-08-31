#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        return (max(a_dictionary, key=lambda i: a_dictionary[i]))
#        maxval = max(a_dictionary, key=a_dictionary.get)
#        return newval
