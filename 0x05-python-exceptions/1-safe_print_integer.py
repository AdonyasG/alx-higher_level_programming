#!/usr/bin/python3
def safe_print_integer(value):
    if value in range(-100000, 100000):
        try:
            print("{:d}".format(value))
            return True
        except ValueError:
            return False
