#!/usr/bin/python3
import sys


def main():
    """Sum up all args assuming args to contains only digs."""

    ssum = 0
    for i, arg in enumerate(sys.argv):
        if i > 0:
            ssum += int(arg)
    print(ssum)


if __name__ == '__main__':
    main()
