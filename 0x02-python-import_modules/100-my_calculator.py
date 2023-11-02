#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def main():
    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    if op == "+":
        print("{} {} {} = {}".format(a, op, b, add(a, b)))
    elif op == "-":
        print("{} {} {} = {}".format(a, op, b, sub(a, b)))
    elif op == "*":
        print("{} {} {} = {}".format(a, op, b, mul(a, b)))
    elif op == "/":
        print("{} {} {} = {}".format(a, op, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)


if __name__ == '__main__':
    main()
