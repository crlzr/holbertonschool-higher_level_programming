#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple1 = tuple_a
    new_tuple2 = tuple_b

    if len(tuple_a) < 2:
        new_tuple1 += (0,) * (2 - len(tuple_a))

    if len(tuple_b) < 2:
        new_tuple2 += (0,) * (2 - len(tuple_b))

    result1 = new_tuple1[0] + new_tuple2[0]
    result2 = new_tuple1[1] + new_tuple2[1]

    return result1, result2

