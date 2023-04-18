#!/usr/bin/python3


import unittest
import json
import os

from models.square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.Ss = Square(1, 2, 3, 4)

    def test_valid_values(self):
        self.assertTrue(Square(1))
        self.assertTrue(Square(123, 5))
        self.assertTrue(Square(144, 12, 31))
        self.assertTrue(Square(100, 2, 32, 400))

    def test_missing_argument(self):
        with self.assertRaises(TypeError):
            Square()

    def test_float_size(self):
        with self.assertRaises(TypeError):
            Square(1.2)

    def test_str_size(self):
        with self.assertRaises(TypeError):
            Square("8")

    def test_tuple_size(self):
        with self.assertRaises(TypeError):
            Square((5,))
        with self.assertRaises(TypeError):
            Square((2,))

    def test_width_equal_to_height(self):
        self.Ss.size = 40
        self.assertEqual(self.Ss.width, self.Ss.height)

    def test_area_method(self):
        self.assertEqual(self.Ss.area(), 1)
        self.Ss.size = 13
        self.assertEqual(self.Ss.area(), 169)
        self.Ss.size = 456
        self.assertEqual(self.Ss.area(), 456*456)
        self.Ss.size = 43
        self.assertEqual(self.Ss.area(), 43*43)


if __name__ == "__main__":
    unittest.main()
