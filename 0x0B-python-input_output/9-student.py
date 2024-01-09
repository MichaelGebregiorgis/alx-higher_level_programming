#!/usr/bin/python3
"""Student class"""


class Student:
    """Represent student class"""

    def __init__(self, first_name, last_name, age):
        """Initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dict of students"""
        return self.__dict__
