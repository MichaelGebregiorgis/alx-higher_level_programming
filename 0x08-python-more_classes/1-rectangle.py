#!/usr/bin/python3
"""Rect class"""


class Rectangle:
    """Rectangle detail"""
    def __init__(self, width = 0, height = 0):
        """initialization"""
        self. height = height
        self.width = width

    @property
    def width(self):
        """width of the rectangle"""
        return (self._width)

    @width.setter
    def width(self, val):
        if val < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        self.__width = val

    @property
    def height(self):
        """Height of the rectangle"""
        return (self.height)
    @height.setter
    def height(self, val):
        if val < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        self.__height = val
