#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        size = 0
        sums = 0
        for line in my_list:
            tup = 1
            for num in line:
                tup *= num
            sums += tup
            size += line[-1]
        return sums / size

    return 0
