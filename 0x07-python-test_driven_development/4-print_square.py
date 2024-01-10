#!/usr/bin/python3
"""square #"""


def print_square(size):
    """print # square"""
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    for inc in range(size):
        [print("#", end="") for col in range(size)]
        print("")
