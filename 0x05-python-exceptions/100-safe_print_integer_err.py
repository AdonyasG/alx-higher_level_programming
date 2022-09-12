#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    if True:
        try:
            print("{:d}".format(value))
            return True
        except (TypeError, ValueError) as err:
            stderr.write("Exception: {}\n".format(err))
            return False
