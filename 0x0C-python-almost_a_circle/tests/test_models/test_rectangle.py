#!/usr/bin/python3
"""Unittest for rectangle(...)
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    """ class Comments """

    def test_id(self):
        r1 = Rectangle(10, 2)
        self.assertTrue(r1.area())

if __name__ == '__main__':
    unittest.main()
