#!/usr/bin/python3
def uppercase(str):
    i = 0
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            letter = ord(char) - ord('a') + ord('A')
        else:
            letter = ord(char)
        print(f"{letter:c}", end="")
    print("")
