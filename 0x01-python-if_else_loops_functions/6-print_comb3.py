#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if j > i:
            print("{0}{1}".format(i, j), end="")
            print(", " if i < 8 else "\n", end="")
