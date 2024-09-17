import unittest
from go.group import Group
from go.stone import Stone
from go.board import Board
from go.constants import BLACK, WHITE

class TestFindStones(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.stone = Stone(self.board, (3,3), BLACK)
        self.stone2 = Stone(self.board, (4,3), BLACK)
        self.stone3 = Stone(self.board, (5,3), BLACK)
        self.stone4 = Stone(self.board, (6,3), WHITE)
        self.stone5 = Stone(self.board, (5,4), WHITE)
        self.stone6 = Stone(self.board, (6,4), BLACK)
        self.stone7 = Stone(self.board, (7,4), WHITE)
        self.stone8 = Stone(self.board, (6,5), BLACK)
          
    def test_single_stone(self):
        self.assertEqual(self.board.find_stones([(3,3)]), [self.stone])
        
    def test_non_existent_stone(self):
        self.assertEqual(self.board.find_stones([(7,6)]), [])
    
    def test_one_neighbouring_stone(self):
        self.assertEqual(self.board.find_stones(self.stone.neighbours()), [self.stone2])
        
    def test_two_neighbouring_stones(self):
        self.assertEqual(self.board.find_stones(self.stone2.neighbours()), [self.stone3, self.stone])
        
    def test_three_neighbouring_stones(self):
        self.assertEqual(self.board.find_stones(self.stone3.neighbours()), [self.stone2, self.stone4, self.stone5])
        
    def test_four_neighbouring_stones(self):
        self.assertEqual(self.board.find_stones(self.stone6.neighbours()), [self.stone4, self.stone5, self.stone8, self.stone7])
    
if __name__ == '__main__':
    unittest.main()