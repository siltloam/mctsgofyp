from .node import Node
from go.stone import Stone
from go.stone_view import StoneView
from go.board import Board
from go.constants import BLACK, WHITE
import copy
from operator import attrgetter

class MCTS():
    """Utility class for the Monte Carlo Tree Search. Creates
    tree structure and performs all functions associated with the method.
    """

    def __init__(self, timestep):
        """Constructor for MCTS class.

        Args:
            timestep (int): tracks the timestep for the search
        """
        self.timestep = timestep
        self.black_wins = 0
        self.white_wins = 0
        self.depth = 0
        
    def play(self, state, simulation_count):
        """Initialises the first node and runs the kernel to return
        the best child node to be played in the real game.

        Args:
            state (Board): The state of the board before the AI move
            simulation_count (int): The user's choice of simulations

        Returns:
            Node: child of the root node with the highest visit count
        """
        play_node = Node(None, state, 0, 0, 1)
        self.kernel(play_node, simulation_count)
        res = max(play_node.children, key=attrgetter('visit_count'))
        return res

    def kernel(self, root, simulation_count):
        """Runs the MCTS steps a give number of times and increases timestep
        for recalculations

        Args:
            root (Node): The root node to begin with
            simulation_count (int): The amount of simulations to perform
        """
        for i in range(simulation_count-1):
            self.depth = 0
            leaf = self.traverse(root)
            rollout_node = self.expand(leaf)
            result = self.rollout(rollout_node)
            self.backpropagate(rollout_node, result)
            self.timestep += 1

    def traverse(self, root):
        """Traverses the tree from a specified node
        (usually the root of the game tree)

        Args:
            root (Node): The root node

        Returns:
            Node: recursively traverses until we reach a leaf node
        """
        if root.children == []:
            return root
        else:
            highest_ucb = 0
            highest_index = None
            for node in root.children:
                cur_ucb = node.get_ucb_val(self.timestep)
                if cur_ucb > highest_ucb:
                    highest_ucb = cur_ucb
                    highest_index = node
            return self.traverse(highest_index)
    
        
    def expand(self, node):
        """Expands a node into all the possible moves
        one step ahead from the current state of the game

        Args:
            node (Node): the node to expand

        Returns:
            Node: Either the node itself or the first child that is created.
        """
    #   if visit count is 0 then just simulate from there
    #   otherwise generate new nodes from the parent of all possible actions
    #   then rollout on the first node that has been created
        if node.visit_count == 0:
            return node
        else:
            for i in range(len(node.actions)):
                # gen new pos
                new_position = node.random_position()
                # check pos would be valid
                if not node.state.find_stones([new_position]) and new_position != None:
                    #TODO: fix this deepcopy
                    cur_node = Node(node, copy.deepcopy(node.state), 0, 0, 0)
                    # print(cur_node.state.groups)
                    cur_node.expansion_move = (new_position[0], new_position[1])
                    # create new stone for pos and update with it
                    # have to update the colour of the node here (to deviate from parent)
                    cur_stone = Stone(cur_node.state, (new_position[0], new_position[1]), cur_node.state.update_turn())
                    # re-update colour of node here after the placement of the stone
                    cur_node.colour = cur_node.state.get_turn()
                    # print(cur_node.colour)
                    cur_node.state.update_board(cur_stone)
                    node.children.append(cur_node)
            return node.children[0]
    
    def rollout(self, node):
        """Simulates a game down to an end state and returns the winner of the game

        Args:
            node (Node): the node to simulate from

        Returns:
            const: Black or white; whoever won the game
        """
        node.simulations += 1
        rollout_node = Node(None, copy.deepcopy(node.state), None, None, None)
        while not rollout_node.state.game_over == True:
            new_coordinate = rollout_node.random_position()
            if new_coordinate == None:
                rollout_node.state.pass_turn()
            if not rollout_node.state.find_stones([new_coordinate]) and new_coordinate != None:
                new_stone = Stone(rollout_node.state, (new_coordinate[0], new_coordinate[1]), rollout_node.state.update_turn())
                rollout_node.state.update_board(new_stone)
        if rollout_node.state.black_points > rollout_node.state.white_points:
            self.black_wins += 1
            return BLACK
        else:
            self.white_wins += 1
            return WHITE
        
    def backpropagate(self, node, result):
        """Updates the value of the current node and recursively
        updates the parents of that node

        Args:
            node (Node): the node to begin the backpropagation
            result (const): the winner of the simulated game
        """
        node.visit_count += 1
        self.depth += 1
        if result == node.colour:
            node.wins += 1
        if node.parent != None:
            self.backpropagate(node.parent, result)