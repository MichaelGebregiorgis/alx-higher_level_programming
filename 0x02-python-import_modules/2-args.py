#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    if length == 0:
        print("0 arguments.")
    elif length > 0:
        if length == 1:
            print(f"{length} argument:")
        else:
            print(f"{length} arguments:")
        for args in range(length):
            print(f"{args + 1}: {sys.argv[args + 1]}")
