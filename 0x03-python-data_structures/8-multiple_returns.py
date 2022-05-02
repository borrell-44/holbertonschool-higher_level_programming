#!/usr/bin/python3
def multiple_returns(sentence):
    tup = (0, None)
    if not sentence:
        return tup
    lis = list(tup)
    lis[1] = sentence[0]
    lis[0] = len(sentence)
    tup = tuple(lis)
    return tup
