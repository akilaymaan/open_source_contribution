"""Calculator example for an open-source contribution demonstration.

Use integers or floats as inputs; this example does not parse keyboard input.
"""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the first number minus the second number."""
    return a - b


# Importing the functions in tests should not run the demonstration.
if __name__ == "__main__":
    print("Addition:", add(10, 5))
    print("Subtraction:", subtract(10, 5))
