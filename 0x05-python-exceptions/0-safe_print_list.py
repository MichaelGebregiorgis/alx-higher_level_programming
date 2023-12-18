#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    val = 0
    for inc in range(x):
        try:
            print("{}".format(my_list[inc]), end="")
            val += 1
        except IndexError:
            break
    print("")
    return (val)
