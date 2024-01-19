#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Repersent values"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialization"""
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return format string"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")
