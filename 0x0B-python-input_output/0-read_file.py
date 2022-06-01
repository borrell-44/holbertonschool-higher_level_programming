#!/usr/bin/python3

""" file Comments """


def read_file(filename=""):

    """ function Comments """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
