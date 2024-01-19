#!/usr/bin/python3
"""Define rectangle"""
from models.base import Base


class Rectangle(Base):
    """Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization"""

        self.height = height
        self.x = x
        self.width = width
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """Height set"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("height must be > 0")
        if type(value) != int:
            raise TypeError("height must be an integer")
        self.__height = value

    @property
    def width(self):
        """Set width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("width must be > 0")
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def x(self):
        """x coordinate"""
        return (self.__x)

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("x must be >= 0")

        if (type(value) is not int):
            raise TypeError("x must be an integer")
        self.__x = value

    @property
    def y(self):
        """y coordinate"""
        return (self.__y)

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("y must be >= 0")

        if (type(value) is not int):
            raise TypeError("y must be an integer")
        self.__y = value
