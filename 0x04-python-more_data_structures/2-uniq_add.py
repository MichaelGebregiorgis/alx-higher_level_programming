#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = []
    sum = 0
    for val in my_list:
        if val not in uniq_list:
            sum = sum + val
            uniq_list.append(val)
    return (sum)
