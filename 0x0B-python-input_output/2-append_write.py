#!/usr/bin/python3

""" file Comments """


def append_write(filename="", text=""):

    """ function Comments """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
