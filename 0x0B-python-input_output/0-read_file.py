#!/usr/bin/python3

""" file Comments """


def read_file(filename=""):

    """ function Comments """

    with open(filename) as f:
        print(f.read(), end="")
