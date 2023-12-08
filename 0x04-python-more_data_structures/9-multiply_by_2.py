#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nDict = {}
    for key, val in a_dictionary.items():
        nDict.update({key: (val * 2)})
    return (nDict)
