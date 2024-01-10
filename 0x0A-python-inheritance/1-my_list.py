#!/usr/bin/python3
"""Contain My list class"""


class MyList(list):
    """subclass"""
    def __init__(self):
        """Initialization"""
        super().__init__()

    def print_sorted(self):
        """sorted list"""
        sorting = sorted(self)
        print(sorting)
