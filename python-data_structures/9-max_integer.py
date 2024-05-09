#!/usr/bin/python3

def max_integer(my_list=[]):
    my_list.sort(reverse=True)

    if my_list == "":
        return 0, None
    else:
        return (my_list[0])
