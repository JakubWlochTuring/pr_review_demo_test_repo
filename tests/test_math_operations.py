import unittest
from math_operations import MathOperations

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(MathOperations.add(2, 3), 5)
        self.assertEqual(MathOperations.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(MathOperations.subtract(5, 2), 3)
        self.assertEqual(MathOperations.subtract(10, 10), 0)

    def test_multiply(self):
        self.assertEqual(MathOperations.multiply(4, 3), 12)
        self.assertEqual(MathOperations.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(MathOperations.divide(10, 2), 5)
        self.assertAlmostEqual(MathOperations.divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            MathOperations.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
