#!/usr/bin/python3
import sys
import argparse


def main():
    """Print args"""

    if len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv) - 1))
    else:
        pname = sys.argv[0]
        parser = argparse.ArgumentParser(
                prog=pname,
                description='print number of and list of arguments')
        parser.add_argument('pargs', nargs='+')
        args = parser.parse_args()
        print(len(args.pargs),
              "argument:" if len(args.pargs) == 1 else "arguments:")
        for i, arg in enumerate(args.pargs, 1):
            print("{}: {}".format(i, arg))


if __name__ == '__main__':
    main()
