#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        if value:
            print("{:d}".format(value))
            return True
    except (TypeError, IndexError, ValueError):
        print("Exception: ")
        return False
