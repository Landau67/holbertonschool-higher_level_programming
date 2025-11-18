#!/usr/bin/python3
def weight_average(my_list=[]):
    s = 0
    b = 0
    n = 0
    for row in my_list:
        s += row[0] * row[1]
        n += row[1]
    b = s / n
    return b
