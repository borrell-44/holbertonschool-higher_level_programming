#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = int(repr(number)[-1])
print("Last digit of {0} is ".format(number), end="")
if number < 0 and last != 0:
 print("-{0} and is less than 6 and not 0".format(last))
elif last < 0 and last < 6:
 print("{0} and is less than 6 and not 0".format(last))
elif last == 0:
 print("{0} and is 0".format(last))
else:
 print("{0} and is greater than 5".format(last))
