#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Rectangle details"""

    def __init__(self, width=0, height=0):
        """Initialization"""
        self.height = height
        self.width = width

        @property
        def height(self):
            """height of the rectangle"""
            return (self.__height)

        @height.setter
        def height(self, value):
            if value < 0:
                raise ValueError("height must be >= 0")
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            self.heigth = value

        @property
        def width(self):
            """Width of the rectangle"""
            return (self.__width)

        @width.setter
        def width(self, value):
            if value < 0:
                raise ValueError("width must be >= 0")
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            self.__width = value
