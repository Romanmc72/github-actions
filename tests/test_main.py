#!/usr/bin/env python3
"""Some unit tests"""
import unittest

from src import main


class TestMainFile(unittest.TestCase):
    def test_always_return_foo(self):
        self.assertEqual(main.always_return_foo(), "foo")

    def test_square_number(self):
        self.assertEqual(main.square_number(2), 4)

    def test_be_annoyed(self):
        self.assertEqual(main.be_annoyed(), "Someone here is annoyed.")

    def test_be_annoyed_input(self):
        self.assertEqual(main.be_annoyed("My dog"), "My dog is annoyed.")


if __name__ == "__main__":
    unittest.main()
