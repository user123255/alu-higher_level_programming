#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_rectangle_id(self):
        r = Rectangle(10, 20, 5)
        self.assertEqual(r.id, 5)

    def test_rectangle_attributes(self):
        r = Rectangle(4, 6)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 6)
