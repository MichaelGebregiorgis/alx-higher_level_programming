#!/usr/bin/python3
"""Addition function"""


def add_integer(a, b=98):
    """a + b"""
    if ((not isinstance(a, int)and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, float) and not isinstance(b, int))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
