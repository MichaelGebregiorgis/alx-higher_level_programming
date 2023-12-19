#!/usr/bin/python3
"""Square class"""


class Square:
    """inside the class"""
    def __init__(self, val=0):
        """Initialization"""
        self.__size = val

    @property
    def size(self):
        """current val"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area"""
        return (self.__size ** 2)
