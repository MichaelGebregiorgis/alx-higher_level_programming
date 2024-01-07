#!/usr/bin/python3
"""Define class"""


class Rectangle:
    """Describe rect"""

    def __init__(self, width=0, height=0):
        """Initialization
        Args:
            width (int): width
            height (int): height
            """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__height = value

    def perimeter(self):
        """return perimeter"""
        if self.width == 0 or self.__height == 0:
            return(0)
        return(2 * (self.__width + self.__height))

    def area(self):
        """Return area"""
        return (self.__width * self.__height)
