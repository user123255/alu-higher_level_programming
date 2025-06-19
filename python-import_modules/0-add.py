#!/usr/bin/python3

from add_0 import add

if __name__ == "__main__":
    a = 1
    b = 2
    
    # Use a single print statement with string format
    try:
        print(f"{a} + {b} = {add(a, b)}")
    except Exception:
        print(f"FAKE add() => {a} - {b}")

    # Additional test cases
    test_cases = [
        (10, 30),
        (-10, 30),
        (-10, -30),
        (5, "H"),
    ]

    for a, b in test_cases:
        try:
            print(f"{a} + {b} = {add(a, b)}")
        except Exception:
            print(f"FAKE add() => {a} - {b}")
