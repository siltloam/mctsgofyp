import unittest
from go.stone import Stone
from go.board import Board
from go.constants import BLACK, WHITE

class TestLiberties(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.stone = Stone(self.board, (3,3), BLACK)
        self.stone2 = Stone(self.board, (5,5), WHITE)
        self.stone3 = Stone(self.board, (5,6), BLACK)
        self.stone5 = Stone(self.board, (1,1), BLACK)
        self.stone6 = Stone(self.board, (9,9), BLACK)

    def test_four_liberties(self):
        self.assertEqual(self.stone.get_liberties(), [(2,3), (3,2), (3,4), (4,3)])

    def test_three_liberties(self):
        self.assertEqual(self.stone2.get_liberties(), [(4,5), (5,4), (6,5)])
                
    def test_top_left_corner_liberties(self):
        self.assertEqual(self.stone5.get_liberties(), [(1,2),(2,1)])
    
    def test_bottom_right_corner_liberties(self):
        self.assertEqual(self.stone6.get_liberties(), [(8,9),(9,8)])
    
        