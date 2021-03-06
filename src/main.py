#!/usr/bin/env python3
"""
Python file with some functions that need to be tested
We should see a few errors from flake8...
...and we did! fixed them.
"""


def always_return_foo() -> str:
    """Literally just returns foo."""
    return "foo"


def square_number(number: int) -> int:
    """Multiplies the number by itself and that is it."""
    return number * number


def be_annoyed(name: str = None):
    if name is None:
        name = "Someone here"
    return f"{name} is annoyed."
