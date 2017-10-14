import unittest
from merge_sort import merge_sort
from bubble_sort import bubble_sort


class SortingTests(unittest.TestCase):
    def test_merge_sort(self):
        self.sort_tester(merge_sort)

    def test_bubble_sort(self):
        self.sort_tester(bubble_sort)

    def sort_tester(self, sort_function):
        array = [2, 3, 1, 5, 6, 4, 0]

        self.assertEqual(sort_function(array), [0, 1, 2, 3, 4, 5, 6])

if __name__ == '__main__':
    unittest.main()
