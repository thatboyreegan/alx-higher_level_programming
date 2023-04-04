#!/usr/bin/python3
"""Defines a function that indents text"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after every '.','?' and ':'

    Args:
        text (str): text to indent

    Raises:
        TypeError: when text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for c in text:
        print(c, end='')
        if c == '.' or c == '?' or c == ':':
            print("\n")
    print("")
