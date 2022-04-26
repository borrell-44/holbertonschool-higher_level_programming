#!/usr/bin/python3
def uppercase(str):
    l = len(str)
    for i in range(0, l):
        c = str[i]
        if ord(c) >= 97 and ord(c) <= 122:
            con = True
        else:
            con = False
        u = chr(ord(c) - 32)
        print("{}".format(u) if con is True else "{}".format(c), end="")
    print()
