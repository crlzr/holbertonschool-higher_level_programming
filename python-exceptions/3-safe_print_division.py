#!/usr/bin/python3

def safe_print_division(a, b):
    result = None
    try:
        result = a / b
        print("{}".format(a / b))
    except (ZeroDivisionError, TypeError, IndexError):
        return None
    finally:
        print("Inside result: {}".format(result))
        return result
