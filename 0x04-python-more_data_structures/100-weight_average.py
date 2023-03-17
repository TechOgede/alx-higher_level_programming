#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    weighted_total = 0
    sum_weights = 0
    for x, y in my_list:
        weighted_total += x * y
        sum_weights += y
    return weighted_total / sum_weights
