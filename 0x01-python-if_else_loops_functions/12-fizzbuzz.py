#!/usr/bin/python3
def fizzbuzz():
    for value in range(1, 101):
        if value % 3 == 0 and value % 5 == 0:
            value = "FizzBuzz"
            print(value, end=' ')
        elif value % 3 == 0:
            value = "Fizz"
            print(value, end=' ')
        elif value % 5 == 0:
            value = "Buzz"
            print(value, end=' ')
        else:
            print(value, end=' ')
