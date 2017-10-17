import unittest
from euclidean_algorithm import euclidean_algorithm


class EuclideanAlgorithmTests(unittest.TestCase):
    def test_multiple(self):
        x = 5
        y = 25
        self.assertEqual(euclidean_algorithm(x, y), 5)
        self.assertEqual(euclidean_algorithm(y, x), 5)

    def test_relatively_prime(self):
        x = 25
        y = 9
        self.assertEqual(euclidean_algorithm(x, y), 1)

    def test_reflexive(self):
        self.assertEqual(euclidean_algorithm(5, 5), 5)

unittest.main()
