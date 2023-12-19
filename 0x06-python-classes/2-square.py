#!/usr/bin/python3
"""square with safety"""


class Square:
    """in the class"""
    def __init__(self, val=0):
        """size with exceptions"""
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be an integer")
        self.__size = val
