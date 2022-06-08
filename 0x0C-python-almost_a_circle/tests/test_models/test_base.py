#!/usr/bin/python3
"""Unittest for class base(...)
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    """ class Comments """

    def test_main(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(89)
        self.assertEqual(b4.id, 89)
        b5 = Base()
        self.assertEqual(b5.id, 4)


if __name__ == '__main__':
    unittest.main()
