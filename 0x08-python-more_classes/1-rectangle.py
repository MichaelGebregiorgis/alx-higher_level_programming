#!/usr/bin/python3
"""Rect class"""


class Rectangle:
    """Rectangle detail"""
    def __init__(self, wid = 0, hgt = 0):
        """initialization"""
        self. hgt = hgt
        self.wid = wid

    @property
    def wid(self):
        """width of the rectangle"""
        return (self._wid)

    @wid.setter
    def wid(self, val):
        if val < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        self.__wid = val

    @property
    def hgt(self):
        """Height of the rectangle"""
        return (self.hgt)
    @hgt.setter
    def hgt(self, val):
        if val < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        self.__hgt = val
