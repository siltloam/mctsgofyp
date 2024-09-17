import unittest
from go.board import Board
from go.stone import Stone
from go.constants import BLACK, WHITE

class TestTurn(unittest.TestCase):

    # testing the turns themselves
    def setUp(self):
        self.board = Board()
    
    def test_turn_zero(self):
        self.assertEqual(self.board.update_turn(), BLACK)
        
    def test_turn_one(self):
        stone1 = Stone(self.board, (1,2), self.board.update_turn())
        self.assertEqual(self.board.update_turn(), WHITE)
    
    def test_turn_two(self):
        stone1 = Stone(self.board, (1,2), self.board.update_turn())
        stone2 = Stone(self.board, (1,5), self.board.update_turn())
        self.assertEqual(self.board.update_turn(), BLACK)
        
    #testing the passing of turns
    
    def test_black_double_pass(self):
        self.assertEqual(self.board.turn, 0)
        self.board.pass_turn()
        self.assertEqual(self.board.update_turn(), WHITE)
        self.board.pass_turn()
        # asserting here that the game has finished
        self.assertTrue(self.board.game_over)
        
    def test_white_double_pass(self):
        self.assertEqual(self.board.turn, 0)
        self.board.update_turn()
        self.board.pass_turn()
        self.board.update_turn()
        self.board.pass_turn()
        self.assertTrue(self.board.game_over)
        
    def test_alternating_pass(self):
        self.assertEqual(self.board.turn, 0)
        self.board.pass_turn()
        self.board.pass_turn()
        self.assertTrue(self.board.game_over)

        
if __name__ == '__main__':
    unittest.main()