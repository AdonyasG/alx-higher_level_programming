#!/usr/bin/python3
def safe_print_integer(value):
    if True:
        try:
            val = int(value)
            print("{:d}".format(value))
            return value
        except ValueError:
            return False
