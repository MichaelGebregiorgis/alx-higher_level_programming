#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = a_dictionary.keys()
    lists = list(keys)

    for dictVal in lists:
        if value == a_dictionary.get(dictVal):
            del a_dictionary[dictVal]
    return (a_dictionary)
