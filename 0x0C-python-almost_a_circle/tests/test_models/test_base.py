#!/usr/bin/python3
"""Unittest for class base(...)
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    """ class Comments """

    def test_auto_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)


if __name__ == '__main__':
    unittest.main()
