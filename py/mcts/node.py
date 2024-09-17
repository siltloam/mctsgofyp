import math
import random

class Node():
    """Class to represent nodes in the Monte Carlo Game Tree.
    """

    def __init__(self, parent, state, wins, simulations, visit_count, expansion_move=None):
        """Class to represent a node in a MCTS tree

        Args:
            parent (Node): Parent node
            state (Board/BoardView): The stored state of a board
            wins (int): Number of wins recorded for the node 
            simulations (int): Simulations recorded for the node
            visit_count (int): Number of visits on the node
            expansion_move (Tuple, optional): If expanded upon, the move that was used for expansion
        """
        # change the children initialisation so that deepcopies aren't horrid
        self.children = []
        self.parent = parent
        self.state = state #the current board position
        self.wins = wins
        self.simulations = simulations
        self.visit_count = visit_count
        self.expansion_move = expansion_move
        self.colour = self.state.get_turn()
        # list comprehension for actions on the board
        self.actions = [(x,y) for x in range(1,10) for y in range(1,10)]

    def get_ucb_val(self, timestep):
        """UCB getter for selecting the best node

        Returns:
            int: infinite if the node hasn't been visited (for exploration purposes),
            UCB value if it has been visited
        """
        #NOTE: important for selecting!
        if self.visit_count == 0:
            return math.inf
        else:
            # calculate the ucb value here
            return (self.wins / self.visit_count) + (math.sqrt(2 * math.log(timestep) / self.visit_count))
    
    def random_position(self):
        #TODO: make this a node method so it can be called dynamically
        """Generates a random position for play in a rollout. In
        the case that there are no more playable positions, method
        returns null.

        Returns:
            Tuple: A random coordinate on the board
        """
        try:
            choice = random.choice(self.actions)
            self.actions.remove(choice)
            return choice
        except IndexError:
            return None