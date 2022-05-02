#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = []
    for i in range(0, len(my_list)):
        copy.append(my_list[i])
    if idx < 0 or idx >= len(my_list):
        return copy
    copy[idx] = element
    return copy
