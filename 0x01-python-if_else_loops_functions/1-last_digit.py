#!/usr/bin/python3
#!/usr/bin/python3
import random
import sys
number = random.randint(-10000, 10000)
last = int(repr(number)[-1])
sys.stdout.write("Last digit of {0} is {1} ".format(number, last))
if last > 5:
	print("and is greater than 5")
elif last == 0:
	print("and is 0")
else:
	print("and is less than 6 and not 0")
