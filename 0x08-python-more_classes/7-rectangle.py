#!/usr/bin/python3
"""Define class"""


class Rectangle:
    """Describe rect"""

    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width=0, height=0):
        """Initialization"""
        type(self).number_of_instances += 1
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

    def __str__(self):
        """Printable #"""
        if self.__height == 0 or self.width == 0:
            return ("")
        else:
            rect = []
            for inc in range(self.__height):
                [rect.append(str(self.print_symbol)) for wid in range(self.__width)]
                if inc != self.__height - 1:
                    rect.append("\n")
            return("".join(rect))

    def __repr__(self):
        """String rep"""
        rt = "Rectangle(" + str(self.__width)
        rt += ", " + str(self.__height) + ")"
        return (rt)

    def __del__(self):
        """delete instance"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
