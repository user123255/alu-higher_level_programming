#!/usr/bin/python3

def is_same_class(obj, a_class):
    """Return True if the object is exactly an instance of the specified class; otherwise False."""
    return type(obj) is a_class

# Example code to test the is_same_class function
if __name__ == "__main__":
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
