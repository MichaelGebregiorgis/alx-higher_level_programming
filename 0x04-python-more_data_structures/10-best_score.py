#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        keys = (a_dictionary.keys())
        lists = list(keys)
        pt = 0
        val = ""
        for i in lists:
            if a_dictionary[i] > pt:
                pt = a_dictionary[i]
                val = i
        return (val)
