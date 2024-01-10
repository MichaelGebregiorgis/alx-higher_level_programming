#!/usr/bin/python3
"""Text function"""


def text_indentation(text):
    """Print after , . ? :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    a = 0
    length = len(text)
    while a < len(length) and text[a] == ' ':
        a += 1

    while a < length:
        if text[a] == "\n" or text[c] in ".:?":
            if text[c] in ".?:":
                print("\n")

            a += 1
            while a < length and text[c] == ' ':
                a += 1
            continue
        a += 1
