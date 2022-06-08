#!/usr/bin/python3
"""Unittest for rectangle(...)
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    """ class Comments """

    def test_attr(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        r1 = Rectangle(1, 2, 3)
        self.assertEqual(r1.x, 3)

if __name__ == '__main__':
    unittest.main()
