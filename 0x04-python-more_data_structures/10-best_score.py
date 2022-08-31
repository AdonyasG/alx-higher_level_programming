#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        newval = max(a_dictionary, key=lambda i: a_dictionary[i])
#        maxval = max(newval)
#        maxval = max(a_dictionary, key=a_dictionary.get)
        return newval
    else:
        return None
