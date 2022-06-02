#!/usr/bin/python3

""" file Comments """


def append_after(filename="", search_string="", new_string=""):
    with open(filename, "r") as f:
        lines = f.readlines()
    lis = []
    
    for l in lines:
        if search_string in l:
            lis.append(l)
            lis.append(new_string)
        else:
            lis.append(l)

    str = ""
    for i in lis:
        str = str + i

    with open(filename, "w") as f:
        f.write(str)
