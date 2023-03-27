#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x <= 0:
        return 0
    try:
        my_list[x - 1]
    except:
        i = 0
        for x in my_list:
            print("{}".format(x), end='')
            i += 1
        print()
        return i
    else:
        for i in range(x):
            print("{}".format(my_list[i]), end='')
        print()
        return x

