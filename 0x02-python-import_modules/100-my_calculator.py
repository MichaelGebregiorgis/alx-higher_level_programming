import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    length = len(sys.argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    op = sys.argv[2]
    val1 = int(sys.argv[1])
    val2 = int(sys.argv[3])
    if op == '+':
        print(f"{val1} + {val2} = {add(val1, val2)}")
    elif op == '-':
        print(f"{val1} - {val2} = {sub(val1, val2)}")
    elif op == '*':
        print(f"{val1} * {val2} = {mul(val1, val2)}")
    elif op == '/':
        print(f"{val1} / {val2} = {div(val1, val2)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
