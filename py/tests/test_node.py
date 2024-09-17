import unittest
import math
from mcts.node import Node
from go.board import Board

class TestNode(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.node1 = Node(None, self.board, 0, 0, 0)
        self.node2 = Node(None, self.board, 3, 10, 15)
        self.node1.children = [self.node2]

    def test_unvisited_node(self):
        self.assertEqual(self.node1.get_ucb_val(1), math.inf)

    def test_visited_node(self):
        self.assertEqual(self.node2.get_ucb_val(24), (3/15) + (math.sqrt(2 * math.log(24) / 15)))

    def test_random_position_bounds(self):
        self.assertTrue(self.node1.random_position()[0] >= 1 and self.node1.random_position()[0] <= 9)
        self.assertTrue(self.node2.random_position()[1] >= 1 and self.node1.random_position()[1] <= 9)
        
    def test_random_position_removal(self):
        choice = self.node1.random_position()
        self.assertTrue(choice not in self.node1.actions)
        