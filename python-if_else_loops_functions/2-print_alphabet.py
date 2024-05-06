#!/usr/bin/python3

letter = ord("a")  # Start with the ASCII code for 'a'
while letter <= ord("z"):  # Continue until the ASCII code for 'z'
    print(chr(letter), end='')  # Print the character corresponding to the current ASCII code
    letter += 1  # Move to the next ASCII code
