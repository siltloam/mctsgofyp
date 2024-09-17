import unittest
from go.stone import Stone
from go.board import Board
from go.stone_view import StoneView
from go.constants import BLACK, WHITE, WHITE_STONE, BLACK_STONE

class TestGetImage(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.stone = StoneView(self.board, (3,3), WHITE)
        self.stone2 = StoneView(self.board, (5,6), BLACK)

    def test_white_stone(self):
        self.assertEqual(self.stone.get_image(), WHITE_STONE)

    def test_black_stone(self):
        self.assertEqual(self.stone2.get_image(), BLACK_STONE)   

    def test_wrong_stone(self):
        self.assertNotEqual(self.stone.get_image(), BLACK_STONE)