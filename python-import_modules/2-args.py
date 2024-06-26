#!/usr/bin/python3
import sys

if __name__ == "__main__":

    num_args = len(sys.argv) - 1

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(num_args))
        for x in range(1, num_args + 1):
            print("{}: {}".format(x, sys.argv[x]))
