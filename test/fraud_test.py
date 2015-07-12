import unittest

from nose.tools import istest

from hackerrank.fraud import Order


class OrderShould(unittest.TestCase):

    def setUp(self):
        self.order = Order("1,3")

    @istest
    def parse_order_id(self):
        self.assertEqual(1, self.order.order_id)

    @istest
    def parse_deal_id(self):
        self.assertEqual(3, self.order.deal_id)


