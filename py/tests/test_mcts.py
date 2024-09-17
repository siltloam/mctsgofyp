import unittest
from go.board import Board
# from go.board_view import BoardView
from go.stone import Stone
from go.constants import BLACK, WHITE
from mcts.node import Node
from mcts.mcts import MCTS
from go.stone_view import StoneView
import time

class TestMCTS(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.board2 = Board()
        self.node1 = Node(None, self.board, 0, 0, 0)
        self.node2 = Node(None, self.board, 0, 0, 0)
        self.node3 = Node(None, self.board, 5, 5, 7)
        self.node4 = Node(None, self.board, 3, 4, 4)
        self.node5 = Node(None, self.board, 2, 2, 2)
        self.node6 = Node(None, self.board, 0, 0, 0)
        self.node7 = Node(None, self.board, 15, 20, 30)
        self.node8 = Node(None, self.board, 7, 11, 14)
        self.node9 = Node(None, self.board, 3, 10, 15)
        self.node10 = Node(None, self.board, 3, 3, 5)
        self.node11 = Node(None, self.board, 2, 5, 6)
        self.node12 = Node(None, self.board2, 0, 0, 0)
        self.node13 = Node(None, self.board2, 0, 0, 1)
        self.tree = MCTS(8)
        self.tree2 = MCTS(31)
        self.tree3 = MCTS(0)
        self.node1.children = [self.node2]
        self.node3.children = [self.node4, self.node5]
        self.node5.children = [self.node6]
        self.node7.children = [self.node8, self.node9]
        self.node8.children = [self.node10, self.node11]
        self.stone1 = Stone(self.board, (3,3), BLACK)
        self.stone2 = Stone(self.board, (1,1), WHITE)
        self.stone3 = Stone(self.board, (5,6), BLACK)
        self.stone4 = Stone(self.board, (1,2), WHITE)

    def test_traverse_one(self):
        # testing a single node with no children
        self.assertEqual(self.tree.traverse(self.node2), self.node2)
    
    def test_traverse_two(self):
        # testing a node with a single child of visit count 0
        self.assertEqual(self.tree.traverse(self.node1), self.node2)
        
    def test_traverse_three(self):
        # testing a node with two children each with ucb vals, followed by
        # another traversal on a node with no visits
        self.assertEqual(self.tree.traverse(self.node3), self.node6)
        
    def test_traverse_four(self):
        # test two consecutive comparisons of ucb and ensure correct traversal
        self.assertEqual(self.tree2.traverse(self.node7), self.node10)
        
    def test_zero_positions(self):
        for i in range(90):
            self.node1.random_position()
        # points are calculated from here to be white's win
        print(self.node1.colour)
        print(self.node1.actions)
        self.assertEqual(self.tree.rollout(self.node1), BLACK)
    
    def test_successful_rollout(self):
        self.assertEqual(type(self.tree.rollout(self.node1)), type(BLACK))
    
    # triangulated this test- confirmed working in prev ver
    # def test_board_copy(self):
    #     self.assertEqual(self.tree.rollout(self.node1, self.board, self.tree.actions), 0)

    def test_expand_one(self):
        self.assertEqual(self.tree.expand(self.node1), self.node1)
    
    def test_expand_two(self):
        print(len(self.node13.actions))
        self.assertEqual(self.tree.expand(self.node13), self.node13.children[0])
        print(len(self.node13.children))
        self.assertTrue(len(self.node13.children) == 81)
        for i in range(len(self.node13.children)):
            self.assertTrue(len(self.node13.children[i].state.groups) <= 2)
        
    def test_expand_three(self):
        #testing that a node with 0 visits returns itself
        self.assertEqual(self.tree3.expand(self.node12), self.node12)
        
    def test_expand_four(self):
        # testing that each child has a single group after expansion    
        self.tree3.expand(self.node13)
        print(self.node13.children[0].state.groups)
        print(self.node13.children[0].children)
        self.assertEqual(len(self.node13.children[0].state.groups), 1)

    def test_expand_five(self):
        # testing all children of root
        self.tree3.expand(self.node13)
        for i in range(len(self.node13.children)):
            self.assertEqual(len(self.node13.children[i].state.groups), 1)
        # further asserting that the positions are different
        self.assertFalse(self.node13.children[0].state.groups[0].stones.pop().coord == self.node13.children[1].state.groups[0].stones.pop().coord)

    def test_expand_six(self):
        tree = MCTS(0)
        board = Board()
        stone = Stone(board, (3,3), BLACK)
        board.update_board(stone)
        root = Node(None, board, 0, 0, 1)
        tree.expand(root)
        tree.rollout(root.children[0])
        print(root.children[0].actions)
        tree.expand(root.children[0])

    def test_get_colour(self):
        self.assertEqual(self.node13.colour, BLACK)

    def test_expand_colour(self):
        self.tree3.expand(self.node13)
        self.assertEqual(self.node13.colour, BLACK)
        for i in range(len(self.node13.children)):
            self.assertEqual(self.node13.children[i].colour, WHITE)

    def test_backpropagate_one(self):
        self.tree3.expand(self.node13)
        self.tree3.backpropagate(self.node13.children[0], None)
        self.assertEqual(self.node13.children[0].visit_count, 1)
        self.assertEqual(self.node13.visit_count, 2)
        # self.assertEqual(self.tree.rollout(self.node13.children[0], self.board), 0)

    def test_backpropagate_two(self):
        self.tree3.expand(self.node13)
        res = self.tree3.rollout(self.node13.children[0])
        self.tree3.backpropagate(self.node13.children[0], res)
        self.assertEqual(self.node13.children[0].visit_count, 1)
        self.assertEqual(self.node13.visit_count, 2)
        self.assertTrue((self.node13.children[0].wins == 0) or (self.node13.children[0].wins == 1))


    def test_kernel_one(self):
        new_stone = Stone(self.board2, (3,3), self.board2.update_turn())
        self.board2.update_board(new_stone)
        self.board2.update_points()
        new_root = Node(None, self.board2, 0, 0, 1)
        self.tree3.kernel(new_root, 250)
        self.assertEqual(len(new_root.children), 80)
        self.assertTrue(new_root.children[0].visit_count > 0)
        self.assertEqual(new_root.visit_count, 250)
        print(self.tree3.black_wins, self.tree3.white_wins)

    def test_kernel_two(self):
        #testing the first move on a board
        mcts = MCTS(0)
        board = Board()
        stone = Stone(board, (3,3), BLACK)
        board.update_board(stone)
        board.update_points()
        root = Node(None, board, 0, 0, 1)
        self.assertEqual(mcts.traverse(root), root)
        self.assertEqual(mcts.expand(root), root.children[0])
        rollout_result = mcts.rollout(root.children[0])
        self.assertTrue(rollout_result == BLACK or rollout_result == WHITE)
        mcts.backpropagate(root.children[0], WHITE)
        self.assertEqual(root.children[0].wins, 1)
        self.assertEqual(root.wins, 0)
        self.assertEqual(root.children[0].visit_count, 1)
        self.assertEqual(root.visit_count, 2)
        self.assertEqual(root.simulations, 0)
        mcts.timestep += 1
        # moving onto the second simulation
        # stone2 = Stone(board, (9,9), BLACK)
        # board.update_board(stone2)
        # board.update_points()
        # root.state = board
        # new_leaf = mcts.traverse(root)
        # self.assertTrue(new_leaf in root.children)

    def test_kernel_three(self):
        mcts = MCTS(0)
        board = Board()
        stone = Stone(board, (3,3), BLACK)
        board.update_board(stone)
        board.update_points()
        root = Node(None, board, 0, 0, 1)
        mcts.expand(root)
        mcts.timestep = 82
        for i in range(len(root.children)):
            root.children[i].visit_count += 1
            root.children[i].simulations += 1
            mcts.expand(root.children[i])
        self.assertTrue(mcts.traverse(root).parent in root.children)
        