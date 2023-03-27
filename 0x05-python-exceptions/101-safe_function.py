#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        res = fct(*args)
    except Exception as exc:
        print("Exception: {}".format(exc), file=sys.stderr)
        res = None
    return res
