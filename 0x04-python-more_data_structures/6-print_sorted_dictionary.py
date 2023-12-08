#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = a_dictionary.keys()
    lists = list(keys)
    lists.sort()
    for val in lists:
        print("{}: {}".format(val, a_dictionary[val]))
