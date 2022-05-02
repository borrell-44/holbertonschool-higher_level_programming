#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = (0, 0)
    c = list(tuple_c)
    if tuple_a:
        if len(tuple_a) >= 2:
            c[1] = tuple_a[1]
        if len(tuple_a) >= 1:
            c[0] = tuple_a[0]

    if tuple_b:
        if len(tuple_b) >= 2:
            c[1] += tuple_b[1]
        if len(tuple_b) >= 1:
            c[0] += tuple_b[0]

    tuple_c = tuple(c)
    return tuple_c
