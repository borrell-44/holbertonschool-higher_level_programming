#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    end = []

    try:
        end = fct(args[0], args[1])
    except (BaseException):
        print("Exception:", sys.exc_info()[1], file=sys.stderr)
        return None

    return end
