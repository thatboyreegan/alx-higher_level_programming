#!/usr/bin/python3

import unittest
import json
import os

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(1, 2, 3, 4, 5)

    def test_valid_values(self):
        self.assertTrue(Rectangle(1, 2))
        self.assertTrue(Rectangle(1, 2, 3))
        self.assertTrue(Rectangle(1, 2, 3, 4))
        self.assertTrue(Rectangle(1, 2, 3, 4, 5))

    def test_missing_argument(self):
        with self.assertRaises(TypeError):
            Rectangle(1)
        with self.assertRaises(TypeError):
            Rectangle()

    def test_float_width_height(self):
        with self.assertRaises(TypeError):
            Rectangle(1.1, 2)
        with self.assertRaises(TypeError):
            Rectangle(1, 2.1)

    def test_tuple_width_height(self):
        with self.assertRaises(TypeError):
            Rectangle((1,), 2)
        with self.assertRaises(TypeError):
            Rectangle(1, (2,))

    def test_list_width_height(self):
        with self.assertRaises(TypeError):
            Rectangle([1], 2)
        with self.assertRaises(TypeError):
            Rectangle(1, [2])

    def test_dict_width_height(self):
        with self.assertRaises(TypeError):
            Rectangle({'width': 1}, 2)
        with self.assertRaises(TypeError):
            Rectangle(1, {})

    def test_zero_width_height(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_negative_width_height(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 4)
        with self.assertRaises(ValueError):
            Rectangle(7, -6)

    def test_float_x_y(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 6.4, 4)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 8.9)

    def test_str_x_y(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "three", 4)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "four")

    def test_list_x_y(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, [], ())

    def test_width_getter_and__setter(self):
        self.r1.width = 3
        self.assertEqual(self.r1.width, 3)

    def test_height_getter_and_setter(self):
        self.r1.height = 7
        self.assertEqual(self.r1.height, 7)

    def test_x_getter_and_setter(self):
        self.r1.x = 67
        self.assertEqual(self.r1.x, 67)

    def __update_assert_loop(self, values):
        for attr, arg in values:
            with self.subTest(attr=attr, arg=arg):
                self.assertEqual(getattr(self.r1, attr), arg)


if __name__ == "__main__":
    unittest.main()
