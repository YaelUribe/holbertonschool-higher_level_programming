#!/usr/bin/python3
"""
text_indentation module:
Function to print a text indenting it
"""


def text_indentation(text):
    """
    Function to print a text indenting with ":, ., ?"
    Parameters:
    -----------
    text : must be a string
    return
    -----------
    Returns the resulting text after indentation
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    if text is None:
        raise ValueError("Text is empty")
    flg = True
    for character in text:
        if flg and character is " ":
            continue
        print(character, end="")
        if character in (".", ":", "?"):
            flg = True
            print()
            print()
        else:
            flg = False
