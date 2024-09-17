import unittest
from go.board import Board
from go.stone import Stone
from go.constants import WHITE, BLACK

class TestNeighbours(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.stone = Stone(self.board, (3,3), BLACK)
        self.stone1 = Stone(self.board, (1,5), WHITE)
        self.stone2 = Stone(self.board, (1,1), BLACK)
        self.stone3 = Stone(self.board, (9,9), WHITE)
    
    def test_neighbours_on_board(self):
        self.assertEqual(self.stone.neighbours(), {(2,3), (3,2), (3,4), (4,3)})
        
    def test_neighbours_side(self):
        self.assertEqual(self.stone1.neighbours(), {(1,6), (2,5), (1,4)})
    
    def test_neighbours_corner(self):
        self.assertEqual(self.stone2.neighbours(), {(1,2), (2,1)})
        
    def test_bottom_right_corner(self):
        self.assertEqual(self.stone3.neighbours(), {(8,9),(9,8)})  
        
if __name__ == '__main__':
    unittest.main()
