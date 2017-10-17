import unittest
from least_common_multiple import least_common_multiple


class LeastCommonMultipleTests(unittest.TestCase):
    def test_multiple(self):
        x = 5
        y = 25
        self.assertEqual(least_common_multiple(x, y), 25)
        self.assertEqual(least_common_multiple(y, x), 25)

    def test_relatively_prime(self):
        x = 25
        y = 9
        self.assertEqual(least_common_multiple(x, y), 9 * 25)

    def test_reflexive(self):
        self.assertEqual(least_common_multiple(5, 5), 5)

unittest.main()
