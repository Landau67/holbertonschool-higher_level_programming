#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for k in range(len(i)):
            if k + 1 == len(i):
                print("{:d}".format(i[k]), end="")
            else:
                print("{:d}".format(i[k]), end=" ")
        print()
