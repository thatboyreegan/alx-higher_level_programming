#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except ValueError as fe:
        print("Exception: {}".format(fe), file=sys.stderr)
        return False
    except TypeError as ne:
        print("Exception: {}".format(ne), file=sys.stderr)
        return False
