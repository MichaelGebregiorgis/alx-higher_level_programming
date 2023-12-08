#!/usr/bin/python3
def weight_average(my_list=[]):
    numer = 0
    denom = 0

    if not my_list:
        return (0)
    for tups in my_list:
        numer = numer + (tups[0] * tups[1])
        denom = denom + tups[1]

    return (numer / denom)
