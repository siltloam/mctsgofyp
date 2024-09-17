import unittest
from go.group import Group
from go.board import Board
from go.stone import Stone
from go.constants import BLACK, WHITE

class TestGroupMerge(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.stone = Stone(self.board, (3,3), BLACK)
        self.stone2 = Stone(self.board, (5,3), BLACK)

    def test_merge_stones(self):
        self.stone.group.merge(self.stone2.group)
        self.assertEqual(self.stone.group.stones, {self.stone, self.stone2})

