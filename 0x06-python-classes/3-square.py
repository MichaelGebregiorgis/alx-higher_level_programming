#!/usr/bin/python3
"""area is added now"""


class Square:
    """inside the class"""
    def __init__(self, val=0):
        """exceprtion"""
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val
    def area(self):
        """area"""
        return (self.__size * self.__size)
