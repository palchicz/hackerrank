import unittest

from nose.tools import istest

from hackerrank.fraud import detect_fraud, Order


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
        self.assert_state_mapped('California', 'ca')
        self.assert_state_mapped('CAlIfoRniA', 'ca')
        self.assert_state_mapped('Illinois', 'il')
        self.assert_state_mapped('New York', 'ny')

    def assert_state_mapped(self, given, expected):
        order = self.get_order(state=given)
        expected_address = '{},{},{},{}'.format(
            self.test_street_address,
            self.test_city,
            expected,
            self.test_zipcode
        )
        self.assertEqual(
            expected_address, order.canonical_address)

    @istest
    def maps_street_address_to_canonical_form(self):
        self.assert_street_address_mapped(
            '123 sesame st.', '123 sesame street')
        self.assert_street_address_mapped(
            '123 sesame rd.', '123 sesame road')
        self.assert_street_address_mapped(
            '123 sesame Rd.', '123 sesame road')
        self.assert_street_address_mapped(
            '123 sesame street', '123 sesame street')
        self.assert_street_address_mapped(
            '123 sesame lane', '123 sesame lane')

    def assert_street_address_mapped(self, given, expected):
        order = self.get_order(street_address=given)
        expected_address = '{},{},{},{}'.format(
            expected,
            self.test_city,
            self.test_state,
            self.test_zipcode
        )
        self.assertEqual(
            expected_address, order.canonical_address)


class DetectFraudShould(unittest.TestCase):

    def get_order(
            self,
            order_id,
            deal_id = '1',
            email = 'test@yahoo.com',
            street_address = '123 sesame stree',
            city = 'oakland',
            state = 'ca',
            zipcode = '93331',
            credit_num = 12345678910):
        csv_record = '{},{},{},{},{},{},{},{}'.format(
            order_id,
            deal_id,
            email,
            street_address,
            city,
            state,
            zipcode,
            credit_num
        )
        return Order(csv_record)

    @istest
    def find_no_fraud_with_no_orders(self):
        self.assertEqual([], detect_fraud([]))

    @istest
    def find_no_fraud_with_one_order(self):
        order = self.get_order(1)
        self.assertEqual([], detect_fraud([order]))

    @istest
    def find_no_fraud_when_deal_ids_differ(self):
        order1 = self.get_order(1, deal_id=1)
        order2 = self.get_order(2, deal_id=2)
        order3 = self.get_order(3, deal_id=1)
        self.assertEqual(
            [1, 3], detect_fraud([order1, order2, order3]))

    @istest
    def find_fraud_with_identical_emails(self):
        order1 = self.get_order(1, zipcode='1111')
        order2 = self.get_order(2, zipcode='2222')
        self.assertEqual([1, 2], detect_fraud([order1, order2]))

    @istest
    def find_fraud_with_colliding_emails(self):
        order1 = self.get_order(
            1, email='elmo@ss.com', zipcode='1111')
        order2 = self.get_order(
            2, email='elmo+10@sS.com', zipcode='2222')
        order3 = self.get_order(
            3, email='El.mo+10@sS.com', zipcode='3333')
        self.assertEqual(
            [1, 2, 3], detect_fraud([order1, order2, order3]))

    @istest
    def find_fraud_with_identical_addresses(self):
        order1 = self.get_order(1, email='a@test.com')
        order2 = self.get_order(2, email='not_a@test.org')
        self.assertEqual([1, 2], detect_fraud([order1, order2]))

    @istest
    def find_fraud_with_colliding_addresses(self):
        order1 = self.get_order(
            1, state='ca', zipcode='12-4', email='a@t.com')
        order2 = self.get_order(
            2, state='CA', zipcode='124', email='b@t.com')
        order3 = self.get_order(
            3, state='CaliForniA', zipcode='1-24', email='c@t.com')
        self.assertEqual(
            [1, 2, 3], detect_fraud([order1, order2, order3]))

    @istest
    def find_fraud_when_email_and_address_identical(self):
        order1 = self.get_order(1)
        order2 = self.get_order(2)
        order3 = self.get_order(3)
        self.assertEqual(
            [1, 2, 3], detect_fraud([order1, order2, order3]))

    @istest
    def find_fraud_when_email_and_address_collide(self):
        order1 = self.get_order(1, zipcode='12', email='a@b.com')
        order2 = self.get_order(2, zipcode='1-2', email='d@e.com')
        order3 = self.get_order(3, zipcode='11', email='f@g.com')
        order4 = self.get_order(4, zipcode='22', email='F@G.cOm')
        self.assertEqual(
            [1, 2, 3, 4],
            detect_fraud([order1, order4, order2, order3])
        )

