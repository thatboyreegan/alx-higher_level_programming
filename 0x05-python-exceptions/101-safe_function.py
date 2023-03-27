#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        fun_c = fct(*args)
        return fun_c
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
