#!/usr/bin/python3
def common_elements(set_1, set_2):
    m = []
    for i in set_1:
        for f in set_2:
            if i == f:
                m.append(i)
    return m

