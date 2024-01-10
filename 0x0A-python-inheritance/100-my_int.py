#!/usr/bin/python3
"""MyInt from int"""


class MyInt(int):
    """Invert operator"""

    def __eq__(self, value):
        """== operator override"""
        return (self.real != value)

    def __ne__(self, value):
        """!= operator override"""
        return (self.real == value))
