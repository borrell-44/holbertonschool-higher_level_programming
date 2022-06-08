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
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.y, 4)
        with self.assertRaises(TypeError) as cm:
            self.assertEqual(Rectangle("1", 2), cm)
        with self.assertRaises(TypeError) as cm:
            self.assertEqual(Rectangle(1, "2"), cm)
        with self.assertRaises(TypeError) as cm:
            self.assertEqual(Rectangle(1, 2, "3"), cm)
        with self.assertRaises(TypeError) as cm:
            self.assertEqual(Rectangle(1, 2, 3, "4"), cm)
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.id, 5)
        with self.assertRaises(ValueError) as cm:
            self.assertEqual(Rectangle(-1, 2), cm)
        with self.assertRaises(ValueError) as cm:
            self.assertEqual(Rectangle(1, -2), cm)
        with self.assertRaises(ValueError) as cm:
            self.assertEqual(Rectangle(0, 2), cm)
        with self.assertRaises(ValueError) as cm:
            self.assertEqual(Rectangle(1, 0), cm)
        with self.assertRaises(ValueError) as cm:
            self.assertEqual(Rectangle(1, 2, -3), cm)
        with self.assertRaises(ValueError) as cm:
            self.assertEqual(Rectangle(1, 2, 3, -4), cm)



if __name__ == '__main__':
    unittest.main()
