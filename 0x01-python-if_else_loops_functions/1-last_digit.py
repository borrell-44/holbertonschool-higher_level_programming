#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = int(repr(number)[-1])
print("Last digit of {:d} is ".format(number), end="")
if number < 0 and last != 0:
    print("-{:d} and is less than 6 and not 0".format(last))
elif last < 0 and last < 6:
    print("{:d} and is less than 6 and not 0".format(last))
elif last == 0:
    print("{:d} and is 0".format(last))
else:
    print("{:d} and is greater than 5".format(last))
