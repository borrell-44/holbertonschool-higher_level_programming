#!/usr/bin/python3
num = 32
for i in range(90, 64, -1):
    u = chr(i + num)
    l = chr(i)
    print("{}".format(u) if num > 0 else "{}".format(l), end="")
    num *= -1
