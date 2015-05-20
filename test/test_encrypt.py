import unittest

from nose.tools import istest

from hackerrank.encrypt import *

class NodeTest(unittest.TestCase):

    @istest
    def get_root_node_test(self):
        encoding_table = {}
        cipher_words = []
        node = get_root_node(cipher_words, encoding_table)
        self.assertEqual(node.index, -1)
        self.assertEqual(node.key, {})
        self.assertEqual(node.candidate, '')

    @istest
    def get_neighbor_when_no_encoding_table(self):
        encoding_table = {}
        cipher_words = ['aa']
        node = get_root_node(cipher_words, encoding_table)
        self.assertEqual(node.neighbors, [])

    @istest
    def get_neighbor_when_no_cipher_words(self):
        encoding_table = {'1':['z']}
        cipher_words = []
        node = get_root_node(cipher_words, encoding_table)
        self.assertEqual(node.neighbors, [])

    @istest
    def get_neighbor_when_no_cipher_words(self):
        encoding_table = {'1':['z']}
        cipher_words = []
        node = get_root_node(cipher_words, encoding_table)
        self.assertEqual(node.neighbors, [])

    @istest
    def get_neighbor_when_no_cipher_words(self):
        encoding_table = {'1':['z']}
        cipher_words = []
        node = get_root_node(cipher_words, encoding_table)
        self.assertEqual(node.neighbors, [])

class FilterCandidatesTest(unittest.TestCase):

    @istest
    def filter_empty_params(self):
        self.assert_filtered([], {}, '', [])
        self.assert_filtered([], {'a' : 'z'}, '', [])

    @istest
    def retains_all_that_completely_match(self):
        self.assert_filtered(['a'], {'a':'z'}, 'z', ['a'])
        self.assert_filtered(['aaa'], {'a':'z'}, 'zzz', ['aaa'])
        self.assert_filtered(
            ['abc'],
            {'a':'z', 'b':'y', 'c':'x'},
            'zyx',
            ['abc']
        )

    @istest
    def retains_all_that_partially_match(self):
        self.assert_filtered(['ab'], {'a':'z'}, 'zy', ['ab'])
        self.assert_filtered(
            ['ab', 'ac', 'ad'],
            {'a':'z'},
            'zy',
            ['ab', 'ac', 'ad'],
        )

    @istest
    def filters_all_that_completely_mismatch(self):
        self.assert_filtered(['a'], {'a':'y'}, 'z', [])
        self.assert_filtered(['a'], {'f':'z'}, 'z', [])
        self.assert_filtered(
            ['az', 'rg'],
            {'f':'z'},
            'ez',
            []
        )
        self.assert_filtered(
            ['az', 'rg'],
            {'a':'k', 'g':'e', 'f':'z'},
            'ez',
            []
        )

    @istest
    def does_not_filter_any_when_empty_table(self):
        self.assert_filtered(
            ['a', 'b', 'c'],
            {},
            'z',
            ['a', 'b', 'c'],
        )

    @istest
    def filters_all_that_partially_mismatch(self):
        self.assert_filtered(
            ['ab', 'mn'],
            {'a':'e', 'n':'f'},
            'zy',
            []
        )
        self.assert_filtered(
            ['aba', 'mnm'],
            {'a':'z', 'b':'e', 'n':'y'},
            'zyz',
            []
        )

    @istest
    def selects_expected_candidates(self):
        self.assert_filtered(
            ['ab', 'mn', 'at'],
            {'a':'z', 'n':'f'},
            'zy',
            ['ab', 'at']
        )
        self.assert_filtered(
            ['aba', 'mnm'],
            {'a':'z', 'n':'t'},
            'zyz',
            ['aba']
        )

    def assert_filtered(self, candidates, table, cipher, expected):
        filtered = filter_candidates(candidates, table, cipher)
        self.assertEqual(filtered, expected)

class TestDecrypt(unittest.TestCase):
    pass

