#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """ class Comments """

    def test_empty(self):
        self.assertEqual(max_integer(), None)

    def test_normal(self):
        self.assertEqual(max_integer([1, 2, 3, 4, ]), 4)

    def test_manyArgs(self):
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_noneList(self):
        self.assertEqual(max_integer("Hello"), 'o')

    def test_None(self):
        self.assertEqual(max_integer([-10, -7, -5, -1]), -1)

if __name__ == '__main__':
    unittest.main()
