import unittest
from go.stone import Stone
from go.board import Board
from go.constants import BLACK, WHITE

class TestUpdatePoints(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        
    def test_zero_stones(self):
        self.assertEqual(self.board.black_points, 0)
        self.assertEqual(self.board.white_points, 5.5)

    def test_black_stone(self):
        stone1 = Stone(self.board, (3,3), BLACK)
        self.assertEqual(self.board.black_points, 1)

    def test_white_stone(self):
        stone2 = Stone(self.board, (1,1), WHITE)
        self.assertEqual(self.board.white_points, 6.5)