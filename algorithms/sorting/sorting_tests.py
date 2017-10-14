import unittest
from merge_sort import merge_sort
from bubble_sort import bubble_sort


class SortingTests(unittest.TestCase):
    def test_merge_sort(self):
        self.sorting_tests(merge_sort)

    def test_bubble_sort(self):
        self.sorting_tests(bubble_sort)

    def sorting_tests(self, sort_function):
        self.sort_tester_all_unequal(sort_function)
        self.sort_tester_all_equal(sort_function)

    def sort_tester_all_unequal(self, sort_function):
        array = [2, 3, 1, 5, 6, 4, 0]
        self.assertEqual(sort_function(array), [0, 1, 2, 3, 4, 5, 6])

    def sort_tester_all_equal(self, sort_function):
        array = [1, 1, 1, 1]
        self.assertEqual(sort_function(array), [1, 1, 1, 1])

unittest.main()
