#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    sumVal = sum(int(args) for args in arguments)
    print(sumVal)
