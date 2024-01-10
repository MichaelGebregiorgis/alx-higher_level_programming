#!/usr/bin/python3
"""inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Insert after each line of string"""
    txt = ""
    with open(filename) as rd:
        for line in rd:
            txt += line
            if search_string in line:
                txt += new_sring
    with open(filename, 'w') as wte:
        wte.write(txt)
