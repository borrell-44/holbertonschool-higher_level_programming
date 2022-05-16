#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    import traceback

    try:
        print("{:d}".format(value))
    except ValueError:
        print("Exception:", sys.exc_info()[1], file=sys.stderr)
        return False

    return True
