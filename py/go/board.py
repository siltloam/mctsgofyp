from .constants import BLACK, WHITE
import pygame
import sys

class Board():
    """Class for the model of the board.
    """
    
    def __init__(self):
        """Initialises the board object, containing a 1D array of groups.
        Komi is set to 5.5.
        """
        self.turn = 0
        self.groups = []
        self.white_points = 5.5
        self.black_points = 0
        self.passes = []
        self.game_over = False
           
    def find_stones(self, coords):
        """Finds stones on the board that correspond to coordinates.
        If nothing found, returns empty array.

        Args:
            coords (List[Tuple]): List of coordinates to find stones for

        Returns:
            List[Stone]: The list of stones for the coordinates
        """
        
        coord_set = set(coords)
        result = [stone for group in self.groups for stone in group.stones if stone.coord in coord_set]
        return result
    
    def get_turn(self):
        """Helper function to return the current colour of the player

        Returns:
            const: Black or white
        """
        if self.turn % 2 == 0:
            return BLACK
        else:
            return WHITE
        
    def update_turn(self):
        """Updates the current turn. Turn alternates from black and white starting with black.

        Returns:
            const: Black or white
        """
        if self.turn % 2 == 0:
            self.turn += 1
            return BLACK
        else:
            self.turn += 1
            return WHITE
        
    def update_points(self):
        """Updates the points of black and white when a new stone is placed.

        Returns:
            int, int: Black's and white's points respectively
        """
        self.white_points = 5.5
        self.black_points = 0
        for group in self.groups:
            for stone in group.stones:
                # print(stone.colour)
                if stone.colour == BLACK:
                    self.black_points += 1
                else:
                    self.white_points += 1
        return self.black_points, self.white_points
    
    def pass_turn(self):
        """Backend function for tracking each players passes.
        Uses an array to store the turns in which players have passed on.

        Returns:
            String: Game over message
        """
        self.passes.append(self.turn)
        # print(self.passes)
        if self.turn % 2 == 0:
            if self.turn - 2 in self.passes:
                self.game_over = True
            elif self.turn - 1 in self.passes:
                self.game_over = True
        else:
            if self.turn - 2 in self.passes:
                self.game_over = True
            elif self.turn - 1 in self.passes:
                self.game_over = True
        self.turn += 1
        
    def update_board(self, new_stone=None):
        """Updates the board. Required to be separate to prevent visual interference.

        Args:
            new_stone (Stone, optional): The new stone placed down
        """
        if new_stone:
            new_stone.group.update_groups()
        for group in self.groups:
            if group != new_stone.group:
                group.update_groups()
        self.update_points()