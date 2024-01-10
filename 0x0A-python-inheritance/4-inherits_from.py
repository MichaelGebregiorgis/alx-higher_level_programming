#!/usr/bin/python3
"""Define inherited function"""


def inherits_from(obj, a_class):
    """Check if inherited"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    else:
        return (False)
