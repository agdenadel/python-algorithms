import unittest
from distance_functions import euclidean_distance


class DistanceFunctionTests(unittest.TestCase):
    def test_euclidean_distance(self):
        self.assertEqual(5.0, euclidean_distance((3, 4), (0, 0)))
        self.assertEqual(0.0, euclidean_distance((1, 1), (1, 1)))
        self.assertEqual(1.0, euclidean_distance((1, 1), (1, 2)))


if __name__ == '__main__':
    unittest.main()
