#!/usr/bin/python3
"""Inherite class checking"""


def is_kind_of_class(obj, a_class):
    """Check inheritance"""
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
