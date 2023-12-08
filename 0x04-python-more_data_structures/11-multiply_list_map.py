#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    mapping = map((lambda a: a * number), my_list)
    listVal = list(mapping)
    return (listVal)
