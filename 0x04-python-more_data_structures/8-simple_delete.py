#!/usr/bin/python3
def simple_delete(a_dictionary, keys=""):
    if a_dictionary:
        if keys in a_dictionary:
            del a_dictionary[keys]
