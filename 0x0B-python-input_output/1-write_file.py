#!/usr/bin/python3

""" file Comments """


def write_file(filename="", text=""):

    """ function Comments """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
