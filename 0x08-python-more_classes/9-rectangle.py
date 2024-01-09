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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """greatest area"""
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """new rect"""
        return (cls(size, size))

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