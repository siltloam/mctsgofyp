import unittest
from go.group import Group
from go.stone import Stone
from go.board import Board
from go.constants import BLACK, WHITE

class TestGroup(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.board2 = Board()
        self.stone = Stone(self.board, (3,3), BLACK)
        self.stone2 = Stone(self.board, (2,3), WHITE)
        self.stone3 = Stone(self.board, (4,3), WHITE)
        self.stone4 = Stone(self.board, (3,4), WHITE)
    
    def test_group_creation(self):
        self.assertEqual(self.stone.group.stones, {self.stone})

    def test_capture_group(self):
        self.assertEqual(len(self.board.groups), 4)
        stone5 = Stone(self.board, (3,2), WHITE)
        self.stone.group.update_groups()
        self.assertEqual(len(self.board.groups), 4)