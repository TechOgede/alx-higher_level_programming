#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cnt = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
        except IndexError:
            break
        except ValueError:
            continue
        except TypeError:
            continue
        else:
            cnt += 1
    print()
    return cnt
