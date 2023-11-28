#!/usr/bin/python3
for char in reversed(range(97, 123)):
    if char % 2 != 0:
        char = char - 32
        print(chr(char), end='')
    else:
        print(chr(char), end='')
