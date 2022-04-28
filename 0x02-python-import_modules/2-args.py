#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("{:d} arguments:".format(len(sys.argv) - 1))
    else:
        print("{:d} arguments.".format(len(sys.argv) - 1))
    for i in range(1, len(sys.argv)):
        print("{:d}: {}".format(len(sys.argv[i]), sys.argv[i]))
