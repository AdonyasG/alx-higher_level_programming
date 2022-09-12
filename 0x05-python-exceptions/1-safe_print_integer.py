#!/usr/bin/python3
def safe_print_integer(value):
    if value is int:
        try:
            return True
        except ValueError:
            return False
