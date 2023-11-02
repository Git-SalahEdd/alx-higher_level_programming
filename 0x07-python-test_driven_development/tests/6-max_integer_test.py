#!/usr/bin/python3
"""Unittest with max_integer([..])
"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test class for max_integer()
    """
    def test_module_doc(self):
        """
        Tests module doctring
        """
        docstring = __import__("6-max_integer").__doc__
        self.assertTrue(len(docstring) > 0)

    def test_function_doc(self):
        """
        Tests module doctring
        """
        docstring = __import__("6-max_integer").max_integer.__doc__
        self.assertTrue(len(docstring) > 0)

    def test_empty_list(self):
        """
        Tests with empty lists
        """
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """
        Tests with 1 element
        """
        self.assertEqual(max_integer([5]), 5)

    def test_2_elements(self):
        """
        Tests with 2 elements
        """
        self.assertEqual(max_integer([5, 2]), 5)

    def test_ascending_order(self):
        """
        Tests with list in ascending order
        """
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_descending_order(self):
        """
        Tests with list in descending order
        """
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_descending_order_neg(self):
        """
        Tests with list in descending order of negatives
        """
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_ascending_order_neg(self):
        """
        Tests with list in ascending order of negatives
        """
        self.assertEqual(max_integer([-5, -4, -3, -2, -1]), -1)

    def test_all_neg_elements(self):
        """
        Tests with all negative elements without 0
        """
        self.assertEqual(max_integer([-5, -3, -1, -4, -2]), -1)

    def test_all_neg_with_0(self):
        """
        Tests with all negative elements plus 0
        """
        self.assertEqual(max_integer([-5, -3, -1, -4, 0, -2]), 0)

    def test_mixed_elements(self):
        """
        Tests with mixed signed elements
        """
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)

    def test_same_elements_not_max(self):
        """
        Tests with multiples that aren't max
        """
        self.assertEqual(max_integer([2, 4, 6, 4, 8]), 8)

    def test_same_max(self):
        """
        Tests with multiples that are max
        """
        self.assertEqual(max_integer([8, 4, 6, 8, 8]), 8)

    def test_listof_0(self):
        """
        Tests with all 0
        """
        self.assertEqual(max_integer([0, 0, 0, 0, 0]), 0)

    def test_large_numbers(self):
        """
        Tests with large numbers
        """
        self.assertEqual(max_integer([1000000, 5000000, 3000000]), 5000000)

    def test_multi_elements(self):
        """
        Tests with many elements
        """
        self.assertEqual(max_integer([-50, 0, 10, -20, 30, -40, 0, 5, 15,
                                      -25, 35, -45, 0, 25, -15, 20, -30, 40,
                                      -10, 50, 0, -5, 45, -35, 30, 0, -20, 10,
                                      -40, 50, -30, 0, 35, -25, 15, -5, 25, 0,
                                      -45, 20, -35, 45, 0, -15, 30, -10, 40,
                                      50, 0, 5, -40, 35, -45, 10, 0, -20, 50,
                                      30, 15, 20, 0, -25, -5, -35, -15, 25, 0,
                                      -50, -40, 5, 30, -20, 98, 35, -10, 20,
                                      45, 10, 0, -30, 15, -25, 25, -5, 0, 40,
                                      -35, 30, -20, 45, 0, -10, 50, -15, 5,
                                      -25, 0, 20, -30, -40, 35, -50, 0, -5,
                                      10, -45, 25, -15, 0, 30, -20, 40, -35,
                                      15]), 98)

    def test_only_floats(self):
        """
        Tests with floats
        """
        self.assertEqual(max_integer([1.53, 6.33, -9.123, 15.2, 6.0]), 15.2)

    def test_mix_floatint(self):
        """
        Tests with a mix of int and float
        """
        self.assertEqual(max_integer([1.53, 2, -19.123, 15.2, -5]), 15.2)


if __name__ == "__main__":
    unittest.main()
