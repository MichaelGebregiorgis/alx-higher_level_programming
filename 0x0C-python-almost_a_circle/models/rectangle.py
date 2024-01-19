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
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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

    def area(self):
        """Area of rectangle"""
        return self.height * self.width

    def display(self):
        """display using #"""
        for y in range(self.y):
            print("")
        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """All info"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.x, self.y,
                                                        self.width,
                                                        self.height))

    def update(self, *args, **kwargs):
        """Argument to attribute"""
        if args and len(args) != 0:
            ar = 0
            for arg in args:
                if ar == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif ar == 1:
                    self.width = arg
                elif ar == 2:
                    self.height = arg
                elif ar == 3:
                    self.x = arg
                elif ar == 4:
                    self.y = arg
                ar += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
