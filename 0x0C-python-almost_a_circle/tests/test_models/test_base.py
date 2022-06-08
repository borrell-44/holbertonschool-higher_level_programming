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
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(89)
        self.assertEqual(b3.id, 89)

    def test_to_json_string(self):
        b1 = Base()
        self.assertEqual(b1.to_json_string(None), '[]')
        self.assertEqual(b1.to_json_string([]), '[]')
        self.assertEqual(b1.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_string(self):
        b1 = Base()
        self.assertEqual(b1.from_json_string(None), [])
        self.assertEqual(b1.from_json_string("[]"), [])
        self.assertEqual(b1.from_json_string(None), [])
        self.assertEqual(b1.from_json_string('[{"id": 89}]'), [{'id': 89}])

if __name__ == '__main__':
    unittest.main()
