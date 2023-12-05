#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy = my_list.copy()
    if idx > len(my_list) - 1 or idx < 0:
        return (my_list)
    else:
        cpy[idx] = element
        return (cpy)
