#!/usr/bin/python3
import sys

if __name__ == "__main__":

    num_args = len(sys.argv) - 1

    if num_args == 0:
        print(0)
    else:
        result = 0
        for x in range(1, num_args + 1):
            result = result + int(sys.argv[x])
        print("{}".format(result))
