#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except NameError:
        return False
    except ValueError:
        return False
    except TypeError:
        return False
