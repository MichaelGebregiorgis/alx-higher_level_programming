#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    length = len(my_list)
    for val in range(length):
        if my_list[val] % 2 == 0:
            new.append(True)
        else:
            new.append(False)
    return (new)
