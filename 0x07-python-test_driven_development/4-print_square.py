#!/usr/bin/python3
"""
This function prints a square of hashes
Returns:
Hash
"""


def print_square(size):
    """print square"""
    if not (isinstance(size, (int))):
        raise TypeError(f"size must be an integer")
    if (isinstance(size, (int)) and size < 0):
        raise ValueError(f"size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print('#', end='')
            print()
