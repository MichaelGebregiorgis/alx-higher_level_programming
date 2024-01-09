#!/usr/bin/python3
"""fILE WRITING"""


def write_file(filename="", text=""):
    """Write into a file"""
    with open(filename, 'w', encoding="utf-8") as w:
        return w.write(text)
