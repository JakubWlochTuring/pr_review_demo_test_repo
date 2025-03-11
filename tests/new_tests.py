import unittest
from utils import add, is_even, reverse_string

class TestUtils(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(100))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(101))

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string(""), "")

if __name__ == '__main__':
    unittest.main()
