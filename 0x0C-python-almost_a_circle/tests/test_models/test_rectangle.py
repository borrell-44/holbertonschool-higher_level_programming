#!/usr/bin/python3
"""Unittest for rectangle(...)
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    """ class Comments """

    def test_id(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def 

if __name__ == '__main__':
    unittest.main()
