#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as exc:
        print("Exception: {}".format(exc))
        return False
    else:
        return True
