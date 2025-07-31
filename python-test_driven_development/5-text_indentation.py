#!/usr/bin/python3
"""
Module that contains text_indentation function
which prints text with two new lines after '.', '?', and ':'.
"""



def text_indentation(text):
    """
    Prints the text with two new lines after each '.', '?', and ':' characters.

    Args:
        text (str): The text to print

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)

    while i < length:
        print(text[i], end="")
        if text[i] in ['.', '?', ':']:
            print("\n")  # Two new lines (one from print and one extra)
            # Skip any spaces after the punctuation
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue
        i += 1
