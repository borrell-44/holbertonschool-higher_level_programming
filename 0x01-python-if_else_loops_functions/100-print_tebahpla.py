#!/usr/bin/python3
num = 32
for i in range(90, 64, -1):
    print("{}".format(chr(i + num)) if num > 0 else "{}".format(chr(i)), end="")
    num *= -1
print()
