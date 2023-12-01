#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    lists = dir(hidden_4)
    for val in lists:
        if val[:2] != "__":
            print(val)
