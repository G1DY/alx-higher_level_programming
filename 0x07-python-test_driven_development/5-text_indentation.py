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

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3], end="")
