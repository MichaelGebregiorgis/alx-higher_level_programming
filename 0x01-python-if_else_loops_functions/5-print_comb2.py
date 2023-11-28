#!/usr/bin/python3
for num in range(0, 100):
    if num == 99:
        break
    print("{}{}".format(int(num / 10), int(num % 10)), end=', ')
print("{}".format(99))
