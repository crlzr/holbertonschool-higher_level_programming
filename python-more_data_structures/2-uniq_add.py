#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = []
    total = 0
    for item in my_list:
        new_list.append(item)
        total += item
    return (total)
