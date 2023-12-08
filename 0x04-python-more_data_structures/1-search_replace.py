#!/usr/bin/python3
def search_replace(my_list, search, replace):
    val_list = []
    for val in my_list:
        if val == search:
            val_list.append(replace)
        else:
            val_list.append(val)
    return (val_list)
