#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        value = 0
        name = ""
        for i in a_dictionary.keys():
            if a_dictionary[i] > value:
                value = a_dictionary[i]
                name = i
    return name
