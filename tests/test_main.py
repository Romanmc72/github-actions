#!/usr/bin/env python3
"""Some unit tests"""
import unittest

from src import main


class TestMainFile(unittest.TestCase):
    def test_always_return_foo(self):
        self.assertEqual(
            main.always_return_foo(),
            "foo"
        )


if __name__ == "__main__":
    unittest.main()
