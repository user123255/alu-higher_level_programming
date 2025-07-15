#!/usr/bin/python3
"""Module that writes a string to a text file (UTF8) and returns the number of characters written."""


def write_file(filename="", text=""):
    """Writes text to a file and returns number of characters written."""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
