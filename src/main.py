#!/usr/bin/env python3
"""
Python file with some functions that need to be tested
We should see a few errors from flake8
"""


def always_return_foo() -> str:
    """Literally just returns foo."""
    return "foo"


def square_number(number: int) -> int:
    """Multiplies the number by itself and that is it."""
    return number * number


def be_annoyed(name: str = None):
    if name is None:
        name = 'Someone here'
    print(f"{name} is annoyed.")

if __name__ == "__main__":
    print(always_return_foo)
    print(square_number(2))
    be_annoyed()
    be_annoyed("Roman")