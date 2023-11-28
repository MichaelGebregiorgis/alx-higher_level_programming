#!/usr/bin/python3
for char in reversed(range(97, 123)):
    if char % 2 != 0:
        char = char - 32
        print("{}".format(chr(char)), end='')
    else:
        print("{}".format(chr(char)), end='')
