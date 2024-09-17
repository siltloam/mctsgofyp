import unittest
from go.stone import Stone
from go.group import Group
from go.board import Board
from go.constants import BLACK, WHITE

class TestFindGroup(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.stone = Stone(self.board, (7,7), BLACK)
        self.stone2 = Stone(self.board, (3,3), BLACK)
        self.stone3 = Stone(self.board, (4,3), BLACK)
        self.stone4 = Stone(self.board, (2,3), WHITE)
        self.stone5 = Stone(self.board, (2,5), WHITE)
        self.stone6 = Stone(self.board, (3,5), WHITE)
        self.stone7 = Stone(self.board, (5,5), WHITE)
        self.stone8 = Stone(self.board, (6,5), WHITE)
        
        self.stone_list = set()
        for i in range(1,9):
            self.stone_list.add(Stone(self.board, (i,9), WHITE))
        
    def test_one_stone_group(self):
        self.assertEqual(self.stone.group.stones, {self.stone})
    
    def test_two_stone_group(self):
        self.assertEqual(self.stone2.group.stones, {self.stone2, self.stone3})
        
    def test_black_white_group(self):
        self.assertNotEqual(self.stone4.group.stones, {self.stone, self.stone2, self.stone4})
    
    # def test_massive_group(self):
    #     for i in range(8):
    #         self.assertEqual(self.stone_list[i].group.stones[0], self.stone_list[0])

    def test_merge_group(self):
        self.assertEqual(self.stone5.group.stones, {self.stone5, self.stone6})
        self.assertEqual(self.stone7.group.stones, {self.stone7, self.stone8})
        # creating the new stone for the merge (pls work)
        stone9 = Stone(self.board, (4,5), WHITE)

        self.assertEqual(stone9.group.stones, {self.stone5, self.stone6, self.stone7, self.stone8, stone9})