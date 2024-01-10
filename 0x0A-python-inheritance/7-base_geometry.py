#!/usr/bin/python3
"""base geometry class"""


class BaseGeometry:
    """Reprsentation"""

    def integer_validator(self, name, value):
        """Validate par"""
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

    def area(self):
        """Exception"""
        raise Exception("area() is not implemented")
