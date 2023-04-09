#!/usr/bin/python3
"""defines a  text indentation function"""


def text_indentation(text):
    """prints a text with 2 new lines after . ? and :

    Args:
        text: a string of texts to be printed
    Raises:
        TypeError: text must be a string

    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
