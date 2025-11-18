#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) != 0:
        s = 0
        b = 0
        n = 0
        for row in my_list:
            s += row[0] * row[1]
            n += row[1]
        b = s / n
        return b
    else:
        return 0
