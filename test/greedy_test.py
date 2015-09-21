import unittest

from nose.tools import istest

from hackerrank.greedy import _find_most_distant_point_in_range, mini_max

class MiniMaxTest(unittest.TestCase):

    @istest
    def p_and_q_equal(self):
        p, q = (10, 10)
        self.assertEqual(q, mini_max([5, 3, 6], p, q))
        self.assertEqual(q, mini_max([5, 10, 6], p, q))

        self.assertEqual(q, mini_max([9, 10, 11], p, q))
        self.assertEqual(q, mini_max([9, 11], p, q))

        self.assertEqual(q, mini_max([10, 12, 11], p, q))
        self.assertEqual(q, mini_max([13, 12, 11], p, q))


    @istest
    def all_values_leq_p_returns_q(self):
        arr = [5, 2, 6, 1]
        p, q = (10, 12)
        self.assertEqual(q, mini_max(arr, p, q))

        arr = [5, 2, 6, 10]
        p, q = (10, 12)
        self.assertEqual(q, mini_max(arr, p, q))


    @istest
    def all_values_geq_q_returns_p(self):
        arr = [5, 9, 6, 10]
        p, q = (2, 4)
        self.assertEqual(p, mini_max(arr, p, q))

        arr = [4, 9, 6, 10]
        p, q = (2, 4)
        self.assertEqual(p, mini_max(arr, p, q))

    @istest
    def give_max_difference_bound_when_arr_has_one_value(self):
        p = 10
        q = 15

        self.assertEqual(q, mini_max([9], p, q))
        self.assertEqual(q, mini_max([10], p, q))
        self.assertEqual(q, mini_max([11], p, q))

        self.assertEqual(q, mini_max([12], p, q))
        self.assertEqual(p, mini_max([13], p, q))

        self.assertEqual(p, mini_max([14], p, q))
        self.assertEqual(p, mini_max([15], p, q))
        self.assertEqual(p, mini_max([16], p, q))


    @istest
    def give_lowest_minimax(self):
        p=10
        q=16
        self.assertEqual(p, mini_max([9, 11, 13, 15, 17], p, q))
        self.assertEqual(p, mini_max([11, 13, 15, 17], p, q))
        self.assertEqual(p, mini_max([9, 11, 13, 15], p, q))


    @istest
    def find_most_distant_point_in_range_test(self):

        actual = _find_most_distant_point_in_range(1, 6, 6, 7)
        self.assertEqual((6, 0), actual)

        actual = _find_most_distant_point_in_range(7, 8, 6, 7)
        self.assertEqual((7, 0), actual)

        actual = _find_most_distant_point_in_range(1, 7, 6, 7)
        self.assertEqual((6, 1), actual)

        actual = _find_most_distant_point_in_range(1, 8, 6, 7)
        self.assertEqual((6, 2), actual)

        actual = _find_most_distant_point_in_range(5, 8, 6, 7)
        self.assertEqual((6, 1), actual)

        actual = _find_most_distant_point_in_range(4, 8, 6, 7)
        self.assertEqual((6, 2), actual)

        actual = _find_most_distant_point_in_range(5, 10, 6, 7)
        self.assertEqual((7, 2), actual)

        actual = _find_most_distant_point_in_range(6, 8, 6, 7)
        self.assertEqual((7, 1), actual)

        actual = _find_most_distant_point_in_range(5, 20, 6, 7)
        self.assertEqual((7, 2), actual)

        actual = _find_most_distant_point_in_range(10, 20, 10, 20)
        self.assertEqual((15, 5), actual) 

        actual = _find_most_distant_point_in_range(10, 15, 10, 20)
        self.assertEqual((12, 2), actual)

        actual = _find_most_distant_point_in_range(15, 20, 10, 20)
        self.assertEqual((17, 2), actual) 

