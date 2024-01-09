#!/usr/bin/python3
"""File appending"""


def append_write(filename="", text=""):
    """Append into a file"""
    with open(filename, 'a', encoding="utf-8") as a:
        return a.write(text)
