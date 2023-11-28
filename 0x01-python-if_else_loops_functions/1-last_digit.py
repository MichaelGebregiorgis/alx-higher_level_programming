#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l = str(number)
s = l[0]
l = l[-1]
if l < "6" and l != "0" or number < 0:
    if s == "-":
        print(f"Last digit of {number} is {s}{l} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {l} and is less than 6 and not 0")
elif l == "0":
    print(f"Last digit of {number} is {l} and is 0")
elif l > "5":
    print(f"Last digit of {number} is {l} and is greater than 5")
