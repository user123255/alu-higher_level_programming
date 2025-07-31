#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer function"""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_positive_and_negative(self):
        self.assertEqual(max_integer([-1, 0, 1]), 1)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_duplicates(self):
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_large_numbers(self):
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)


if __name__ == '__main__':
    unittest.main()

