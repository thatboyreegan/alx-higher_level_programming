#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    real = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end=" ")
            real += 1
        except ValueError:
            continue
        except TypeError:
            continue
    print("")
    return real
