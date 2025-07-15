#!/usr/bin/python3
"""Module to read and print text from file"""

def read_file(filename=""):
    """Reads a UTF-8 text file and prints to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
