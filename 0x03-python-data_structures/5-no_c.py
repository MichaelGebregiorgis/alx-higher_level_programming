#!/usr/bin/python3
def no_c(my_string):
    map = {ord('C'): None, ord('c'): None}
    new = my_string.translate(map)
    return (new)
