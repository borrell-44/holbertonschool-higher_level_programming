#!/usr/bin/python3
def uppercase(str):
    l = len(str)
    for i in range(0, l):
        c = str[i]
        if ord(c) >= 97 and ord(c) <= 122:
            u = chr(ord(c) - 32)
            print("{}".format(u) if i != l-1 else "{}\n".format(u), end="")
        else:
            print("{}".format(c) if i != l-1 else "{}\n".format(c), end="")
