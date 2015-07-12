import unittest

from nose.tools import istest

from hackerrank.fraud import Order


class OrderShould(unittest.TestCase):

    def setUp(self):
        self.test_order_id = 1
        self.test_deal_id = 3
        self.test_email = 'bugs@bunny.com'
        self.test_street_address = '123 sesame street'
        self.test_city = 'chevy chase'
        self.test_state = 'ca'
        self.test_zipcode = '123456789'
        self.test_address = '{},{},{},{}'.format(
                self.test_street_address,
                self.test_city,
                self.test_state,
                self.test_zipcode
        )
        def get_order(
                order_id = self.test_order_id,
                deal_id = self.test_deal_id,
                email = self.test_email,
                street_address = self.test_street_address,
                city = self.test_city,
                state = self.test_state,
                zipcode = self.test_zipcode):
            csv_record = '{},{},{},{},{},{},{}'.format(
                order_id,
                deal_id,
                email,
                street_address,
                city,
                state,
                zipcode
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
        self.assertEqual(self.test_email, order.canonical_email)

    @istest
    def have_lowercase_canonical_email_address(self):
        order = self.get_order(email='BuGs@BunNy.CoM')
        self.assertEqual(self.test_email, order.canonical_email)

    @istest
    def strip_plus_sign_suffixes_from_email_username(self):
        order = self.get_order(email='bugs+1@bunny.com')
        self.assertEqual(self.test_email, order.canonical_email)

        order = self.get_order(email='bugs+1moreStuff@bunny.com')
        self.assertEqual(self.test_email, order.canonical_email)

    @istest
    def not_strip_plus_sign_suffixes_from_email_domain(self):
        expected_email = 'bugs@bun+ny.com'
        order = self.get_order(email=expected_email)
        self.assertEqual(expected_email, order.canonical_email)

    @istest
    def ignore_periods_in_email_username(self):
        order = self.get_order(email='b..u.gs@bunny.com')
        self.assertEqual(self.test_email, order.canonical_email)

        order = self.get_order(email='bu.gs+1moreS.tuff@bunny.com')
        self.assertEqual(self.test_email, order.canonical_email)

    @istest
    def not_ignore_periods_in_email_domain(self):
        expected_email = 'bugs@bun.ny.com'
        order = self.get_order(email=expected_email)
        self.assertEqual(expected_email, order.canonical_email)

    @istest
    def parse_canonical_address(self):
        order = self.get_order()
        self.assertEqual(
            self.test_address, order.canonical_address)

    @istest
    def have_lower_case_canonical_address(self):
        order = self.get_order(
            street_address = '123 sEsaMe STReEt',
            city = 'CheVy ChaSE',
            state = 'Ca'
        )
        self.assertEqual(
            self.test_address, order.canonical_address)

    @istest
    def strip_dashes_from_the_zipcode(self):
        order = self.get_order(zipcode='12-34--5-67-89-')
        self.assertEqual(
            self.test_address, order.canonical_address)

    @istest
    def map_states_to_canonical_form(self):
        order = self.get_order(state='California')
        self.assertEqual(
            self.test_address, order.canonical_address)

        order = self.get_order(state='CaLiforniA')
        self.assertEqual(
            self.test_address, order.canonical_address)

        order = self.get_order(state='Illinois')
        expected_address = '{},{},{},{}'.format(
            self.test_street_address,
            self.test_city,
            'il',
            self.test_zipcode
        )
        self.assertEqual(
            expected_address, order.canonical_address)

        order = self.get_order(state='New York')
        expected_address = '{},{},{},{}'.format(
            self.test_street_address,
            self.test_city,
            'ny',
            self.test_zipcode
        )
        self.assertEqual(
            expected_address, order.canonical_address)
