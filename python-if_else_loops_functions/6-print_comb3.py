#!/usr/bin/python3

for digit1 in range(0, 9):
    for digit2 in range(digit1 + 1, 10):
        if digit1 == 8 and digit2 == 9:
            print("{}{}".format(digit1, digit2))
        else:
            print("{}{}, ".format(digit1, digit2), end="")

# Add a newline character at the end of the file
