#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    for args in range(length):
        nArg = args + 1
        if args > 0:
            print(f"{int(sys.argv[args]) + int(sys.argv[nArg])}")
