#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic = {}

    if a_dictionary:
        for i in a_dictionary.keys():
            dic[i] = a_dictionary[i] * 2

    return dic
