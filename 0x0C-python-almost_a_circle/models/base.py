#!/usr/bin/python3


class Base:
    """main base"""
    __nb_objects = 0
    def _init__(self, id=None):
        """initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
