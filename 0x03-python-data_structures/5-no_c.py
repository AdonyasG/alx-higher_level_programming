#!/usr/bin/python3
def no_c(my_string):
    if 'c' or 'C' in my_string:
        i = ""
        for c in range(len(my_string)):
            if 'C' != my_string[c] and 'c' != my_string[c]:
                i += my_string[c]
    return i
