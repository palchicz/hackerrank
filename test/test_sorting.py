import unittest

from nose.tools import istest

from hackerrank import sorting

class InsertionSort(unittest.TestCase):

    @istest
    def one_element(self):
        self.assert_sort_steps([1], [[1]])

    @istest
    def two_elements_not_sorted(self):
        self.assert_sort_steps([2, 1], [[2, 2], [1, 2]])

    @istest
    def two_elements_already_sorted(self):
        self.assert_sort_steps([1, 2], [[1, 2]])

    @istest
    def two_elements_with_repeats(self):
        self.assert_sort_steps([2, 2], [[2, 2]])

    @istest
    def three_elements(self):
        steps = [
                    [2, 4, 4],
                    [2, 3, 4]
                ]

        self.assert_sort_steps([2, 4, 3], steps)
        steps = [
                    [2, 4, 4],
                    [2, 2, 4],
                    [1, 2, 4]
                ]
        self.assert_sort_steps([2, 4, 1], steps)

    @istest
    def three_elements_already_sorted(self):
        steps = [[2, 4, 5]]
        self.assert_sort_steps([2, 4, 5], steps)

    @istest
    def three_elements_with_repeats(self):
        steps = [[2, 2, 3]]
        self.assert_sort_steps([2, 2, 3], steps)

        steps = [[2, 2, 2]]
        self.assert_sort_steps([2, 2, 2], steps)

        steps = [[1, 2, 2]]
        self.assert_sort_steps([1, 2, 2], steps)

        steps = [[1, 1, 1], [1, 1, 1], [0, 1, 1]]
        self.assert_sort_steps([1, 1, 0], steps)

    def assert_sort_steps(self, arr, expected_steps):
        answer_gen = sorting.sort_last_elem(arr)
        for i, answer in enumerate(answer_gen):
            self.assertEquals(expected_steps[i], answer)
