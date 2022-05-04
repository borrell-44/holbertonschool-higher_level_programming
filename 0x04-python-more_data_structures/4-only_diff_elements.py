#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    uncommon = []

    if set_1:
        for i in set_1:
            if i not in set_2:
                uncommon.append(i)

    if set_2:
        for j in set_2:
            if j not in set_1:
                uncommon.append(j)

    return uncommon
