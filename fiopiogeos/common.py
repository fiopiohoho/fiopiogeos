"""The common module contains common functions and classes used by the other modules.
"""

def hello_world():
    """Prints "Hello World!" to the console.
    """
    print("Hello World!")


import random

def random_number():
    """
    Generates a random number between 1 and 100.
    Returns:
        int: A random integer.
    """
    return random.randint(1, 1000)

# Example usage
print(random_number())


