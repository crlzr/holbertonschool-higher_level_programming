#!/usr/bin/python3
"""
Writing Unittests for the given function
"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_at_start(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_at_middle(self):
        self.assertEqual(max_integer(([1, 2, 5, 3, 4])), 5)

if __name__ == '__main__':
    unittest.main()
