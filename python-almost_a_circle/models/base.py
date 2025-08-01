# tests/test_base.py

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def setUp(self):
        # Reset counter before each test to keep them independent
        Base._Base__nb_objects = 0

    def test_id_auto_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_manual(self):
        b = Base(99)
        self.assertEqual(b.id, 99)

if __name__ == '__main__':
    unittest.main()
