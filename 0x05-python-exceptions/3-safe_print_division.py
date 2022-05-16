#!/usr/bin/python3
def safe_print_division(a, b):
    num = None
    try:
        num = a / b
    except ValueError:
        num = None
    finally:
        print("Inside result: {}".format(num))
        return num
