#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        for key, val in a_dictionary.items():
            if val == value:
                del a_dictionary[key]
                return a_dictionary

    return a_dictionary
