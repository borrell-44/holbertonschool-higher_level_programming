#!/usr/bin/python3

""" file Comments """


def append_after(filename="", search_string="", new_string=""):

    """ function Comments """

    with open(filename, "r") as f:
        lines = f.readlines()
    lis = []

    for lin in lines:
        if search_string in lin:
            lis.append(lin)
            lis.append(new_string)
        else:
            lis.append(lin)

    str = ""
    for i in lis:
        str = str + i

    with open(filename, "w") as f:
        f.write(str)
