def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        copy1 = my_list.copy()
        return copy1
    else:
        copy = my_list.copy()
        my_list[idx] = element
        return copy
