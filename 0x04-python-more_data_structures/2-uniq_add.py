#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    num = 0

    if my_list:
        for i in my_list:
            if i not in new_list:
                num += i
                new_list.append(i)
    return num
