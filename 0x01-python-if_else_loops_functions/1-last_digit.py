#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = str(number)
s = a[0]
a = a[-1]
if a < "6" and a != "0" or number < 0:
    if s == "-":
        print(f"Last digit of {number} is {s}{a} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {a} and is less than 6 and not 0")
elif a == "0":
    print(f"Last digit of {number} is {a} and is 0")
elif a > "5":
    print(f"Last digit of {number} is {a} and is greater than 5")
