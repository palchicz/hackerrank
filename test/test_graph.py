import unittest

from nose.tools import istest

from hackerrank import graph

class ConvertToTree(unittest.TestCase):

    @istest
    def test_single_node(self):
        g = { 1: set() }
        tree = graph.convert_to_tree(g)
        self.assertEquals(g, tree)

    @istest
    def test_two_nodes(self):
        g = { 1: [2], 2: [1] }
        tree = graph.convert_to_tree(g, 1)
        expected = {1: set([2]), 2: set()}
        self.assertEquals(expected, tree)

        tree = graph.convert_to_tree(g, 2)
        expected = {2: set([1]), 1: set()}
        self.assertEquals(expected, tree)

    @istest
    def test_three_nodes(self):
        g = { 1: [2], 2:[1, 3], 3:[2] }
        tree = graph.convert_to_tree(g, 1)
        expected = {1: set([2]), 2: set([3]), 3: set()}
        self.assertEquals(expected, tree)

        tree = graph.convert_to_tree(g, 3)
        expected = {3: set([2]), 2: set([1]), 1: set()}
        self.assertEquals(expected, tree)

        tree = graph.convert_to_tree(g, 2)
        expected = {2: set([1, 3]), 1: set(), 3: set()}
        self.assertEquals(expected, tree)

class ConvertEdgesToGraph(unittest.TestCase):

    @istest
    def zero_edges_make_empty_graph(self):
        self.assert_correct_graph([], {})

    @istest
    def one_edge_has_reciprocal(self):
        edges = [(1, 2)]
        expected = {1: set([2]), 2:set([1])}
        self.assert_correct_graph(edges, expected)

    @istest
    def reciprocal_input_does_not_cause_duplicates(self):
        edges = [(1, 2), (2, 1)]
        expected = {1: set([2]), 2:set([1])}
        self.assert_correct_graph(edges, expected)

    @istest
    def two_disjoint_edges_have_reciprocals(self):
        edges = [(1, 2), (3, 4)]
        expected = {
                1: set([2]), 2: set([1]),
                3: set([4]), 4: set([3])
        }
        self.assert_correct_graph(edges, expected)

    @istest
    def overlapping_edges_have_reciprocals(self):
        edges = [(1, 2), (2, 4)]
        expected = { 1: set([2]), 2: set([1, 4]), 4: set([2])}
        self.assert_correct_graph(edges, expected)

    @istest
    def overlapping_duplicate_edges_have_reciprocals(self):
        edges = [(1, 2), (2, 4), (4, 2)]
        expected = { 1: set([2]), 2: set([1, 4]), 4: set([2])}
        self.assert_correct_graph(edges, expected)

    def assert_correct_graph(self, edges, expected):
        g = graph.convert_edges_to_graph(edges)
        self.assertEquals(expected, g)

class GetSubtreeSizes(unittest.TestCase):

    @istest
    def size_of_empty_graph(self):
        self.assert_correct_sizes([], None, {})

    @istest
    def count_one_edge_tree(self):
        edges = [('A', 'B')]
        expected = {'A': 2, 'B':1}
        self.assert_correct_sizes(edges, 'A', expected)
        expected = {'B': 2, 'A':1}
        self.assert_correct_sizes(edges, 'B', expected)

    @istest
    def count_two_edge_tree(self):
        edges = [('A', 'B'), ('B', 'C')]
        expected = {'A': 3, 'B':2, 'C': 1}
        self.assert_correct_sizes(edges, 'A', expected)

        expected = {'B': 3, 'A':1, 'C': 1}
        self.assert_correct_sizes(edges, 'B', expected)

        expected = {'C': 3, 'B':2, 'A': 1}
        self.assert_correct_sizes(edges, 'C', expected)

    @istest
    def count_straight_three_edge_tree(self):
        edges = [('A', 'B'), ('B', 'C'), ('C', 'D')]
        expected = {'A': 4, 'B':3, 'C': 2, 'D': 1}
        self.assert_correct_sizes(edges, 'A', expected)

        expected = {'B': 4, 'A':1, 'C': 2, 'D': 1}
        self.assert_correct_sizes(edges, 'B', expected)

        expected = {'C': 4, 'B':2, 'A': 1, 'D': 1}
        self.assert_correct_sizes(edges, 'C', expected)

        expected = {'D': 4, 'C':3, 'B': 2, 'A': 1}
        self.assert_correct_sizes(edges, 'D', expected)

    @istest
    def count_star_three_edge_tree(self):
        edges = [('A', 'B'), ('A', 'C'), ('A', 'D')]
        expected = {'A': 4, 'B': 1, 'C':1, 'D':1}
        self.assert_correct_sizes(edges, 'A', expected)

        expected = {'B': 4, 'A': 3, 'C':1, 'D':1}
        self.assert_correct_sizes(edges, 'B', expected)

    @istest
    def picks_root(self):
        edges = [('A', 'B')]
        g = graph.convert_edges_to_graph(edges)
        sizes = graph.get_subtree_sizes(g)
        expected1 = {'B': 2, 'A':1}
        expected2 = {'B': 1, 'A':2}
        self.assertTrue(sizes in (expected1, expected2))

    def assert_correct_sizes(self, edges, root, expected):
        g = graph.convert_edges_to_graph(edges)
        sizes = graph.get_subtree_sizes(g, root)
        self.assertEquals(expected, sizes)
