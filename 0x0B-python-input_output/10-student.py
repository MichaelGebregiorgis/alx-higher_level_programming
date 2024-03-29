#!/usr/bin/python3
"""Student class"""


class Student:
    """Class representation"""

    def __init__(self, first_name, last_name, age):
        """Initialization"""
        self.age = age
        self.firsst_name = first_name
        self.last_name = last_name

    def to_json(self, attrs=None):
        """Dctionary of student class"""
        if(type(attrs) == list
                and all(type(ele) == str for ele in attrs)):
            return ({x: getattr(self, x) for x in attrs if hasattr(self, x)})
        if attrs is None:
            return (self.__dict__)
