#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= len(str) or n < 0:
        return str
    temp = ""
    for i, letter in enumerate(str):
        if i != n:
            temp += letter
    return temp
