#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}
    result = 0

    if not isinstance(roman_string, str):
        return 0

    for i in range(len(roman_string)):
        value = roman_numerals.get(roman_string[i], 0)
        if (i + 1 < len(roman_string) and
                roman_numerals.get(roman_string[i + 1], 0) > value):
            result -= value
        else:
            result += value

    return result
