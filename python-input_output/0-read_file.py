#!/usr/bin/python3
"""Module that defines read_file function."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints its contents to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
