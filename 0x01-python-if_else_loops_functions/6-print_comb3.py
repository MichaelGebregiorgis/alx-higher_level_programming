#!/usr/bin/python3
for d1 in range(0, 10):
    for d2 in range(d1 + 1, 10):
        if d2 == 9 and d1 == 8:
            print("{}{}".format(d1, d2))
        else:
            print("{}{}".format(d1, d2), end=', ')
