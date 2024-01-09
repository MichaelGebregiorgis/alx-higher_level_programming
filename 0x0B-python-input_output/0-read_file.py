#!/usr/bin/python3
"""file reading"""


def read_file(filename=""):
    """Contents of file"""
    with open(filename, 'r', encoding="utf-8") as r:
        print(r.read(), end="")
