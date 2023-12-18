#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    val = 0
    for inc in range(x):
        try:
            print("{:d}".format(my_list[inc]), end="")
            val += 1
        except (TypeError, ValueError):
            continue
    print("")
    return (val)
