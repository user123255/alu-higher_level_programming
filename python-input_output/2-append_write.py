#!/usr/bin/python3
"""Module that appends a string at the end of a text file and returns the number of characters added."""

def append_write(filename="", text=""):
    """Appends text to a file and returns number of characters written."""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
