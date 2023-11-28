#!/usr/bin/python3
"""Unittest module for the max_integer(list=[]) in 6-max_integer module."""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInt(unittest.TestCase):
    """Unittest testclass."""
    def test_max_integer(self):
        self.assertEqual(max_integer([5, -2, 100, 3]), 100)
        self.assertEqual(max_integer([50, 51, 50, 49]), 51)
        self.assertEqual(max_integer([-10, -5, -2, -1]), -1)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_zero_number(self):
        self.assertEqual(max_integer([0, 0]), 0)

    def test_repeated_number(self):
        self.assertEqual(max_integer([1000, 1000, 1000]), 1000)

    def test_max_operated_integer(self):
        self.assertEqual(max_integer([-3, -5 * -5, 12, -1]), 25)

    def test_big_list(self):
        self.assertEqual(max_integer([
            901, 902, 903, 904, 905, 906, 907, 908, 909, 910,
            919, 918, 917, 1000, 915, 914, 913, 912, 911, 910,
            909, 908, 907, 906, 905, 904, 903, 902, 901]), 1000)

    def test_list_with_loop(self):
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer([i * 5 for i in my_list]), 25)

    def test_one_number_in_a_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_string_number_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([0, '1'])

    def test_tuple_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([10, (20, 30)])

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'key1': 1, 'key2': 2})

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(1)
