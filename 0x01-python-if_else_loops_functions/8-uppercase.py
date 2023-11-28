#!/usr/bin/python3
def uppercase(str):
    for letter in range(len(str)):
        if ord(str[letter]) >=97 and ord(str[letter]) <= 122:
            print("{}".format(chr(ord(str[letter]) - 32)), end='')
        else:
            print("{}".format(str[letter]), end='')
