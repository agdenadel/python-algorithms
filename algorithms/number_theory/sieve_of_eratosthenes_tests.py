import unittest
from sieve_of_eratosthenes import sieve_of_eratosthenes


class LeastCommonMultipleTests(unittest.TestCase):
    def test_small(self):
        n = 10
        self.assertEqual(sieve_of_eratosthenes(n), [2, 3, 5, 7])

    def test_medium(self):
        n = 100
        self.assertEqual(sieve_of_eratosthenes(n), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                                                    43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])


unittest.main()
