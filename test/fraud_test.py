import unittest

from nose.tools import istest

from hackerrank.fraud import Order


class OrderShould(unittest.TestCase):

    def setUp(self):
        self.test_order_id = 1
        self.test_deal_id = 3
        self.test_email = 'bugs@bunny.com'
        def get_order(
                order_id = self.test_order_id,
                deal_id = self.test_deal_id,
                email = self.test_email):
            csv_record = '{},{},{}'.format(
                order_id,
                deal_id,
                email
            )
            return Order(csv_record)
        self.get_order = get_order

    @istest
    def parse_order_id(self):
        order = self.get_order()
        self.assertEqual(self.test_order_id, order.order_id)

    @istest
    def parse_deal_id(self):
        order = self.get_order()
        self.assertEqual(self.test_deal_id, order.deal_id)

    @istest
    def parse_canonical_email_address(self):
        order = self.get_order()
        self.assertEquals(self.test_email, order.canonical_email)

    @istest
    def have_lowercase_canonical_email_address(self):
        order = self.get_order(email='BuGs@BunNy.CoM')
        self.assertEquals(self.test_email, order.canonical_email)

    @istest
    def strip_plus_sign_suffixes_from_email_username(self):
        order = self.get_order(email='bugs+1@bunny.com')
        self.assertEquals(self.test_email, order.canonical_email)

        order = self.get_order(email='bugs+1moreStuff@bunny.com')
        self.assertEquals(self.test_email, order.canonical_email)

    @istest
    def not_strip_plus_sign_suffixes_from_email_domain(self):
        ok_email = 'bugs@bun+ny.com'
        order = self.get_order(email=ok_email)
        self.assertEquals(ok_email, order.canonical_email)

