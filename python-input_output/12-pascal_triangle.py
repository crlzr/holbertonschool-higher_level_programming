#!/usr/bin/python3
"""returns a list of ints representing Pascal's triangle"""


def pascal_triangle(n):
    """Returns list to represent Pascal's triangle"""

    if n <= 0:
        return []

    result = []
    temp = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if i == 0 or j == 0 or i == j:
                row.append(1)
            else:
                row.append(temp[j] + temp[j - 1])
        temp = row
        result.append(row)
    return result
