#!/usr/bin/python3
"""add attribute"""


def add_attribute(obj, att, value):
    """Add new attr"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
