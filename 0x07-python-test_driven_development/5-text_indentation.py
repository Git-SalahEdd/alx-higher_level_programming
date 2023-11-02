#!/usr/bin/python3
"""Module to prints a text with
    2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Function that prints a text with
    2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be processed by the function.

    Raises:
        TypeError: text must be a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    delims = [".", "?", ":"]
    new_text = []
    line = ""
    for char in text:
        line += char
        if char in delims:
            new_text.append(line.replace(" \n", "\n").replace("\n ", "\n"))
            line = ""
    else:
        if line != "":
            new_text.append(line.replace(" \n", "\n").replace("\n ", "\n"))
    for line in new_text:
        print(line.strip(" \t"), end="")
        for el in delims:
            if el in line:
                print(end="\n\n")
                break
