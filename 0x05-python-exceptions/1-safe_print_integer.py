#!/usr/bin/python3
def safe_print_integer(value):
    if True:
        try:
            val = int(value)
            print("{:d}".format(value))
            return True
        except ValueError:
            return False
        return value
