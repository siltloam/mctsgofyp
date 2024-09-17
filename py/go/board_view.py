from go.board import Board
from .constants import BLACK, SQUARE_SIZE, BACKGROUND, WINDOW
import pygame

class BoardView(Board):
    """A class to represent the front-end for a board.

    Args:
        Board (Board): The model for the board that is inherited
    """
    
    def __init__(self):
        """Initialises the visual outline for the board and runs draw method.
        """
        super().__init__()
        self.outline = pygame.Rect(90,90,720,720)
        self.draw_board(WINDOW)
    
    def draw_board(self, window):
        """Draws the Go board on the window

        Args:
            window (pygame.display): The window we are drawing the board on
        """
        pygame.draw.rect(BACKGROUND, BLACK, self.outline, 3)
        for i in range(8):
            for j in range(8):
                rect = pygame.Rect(SQUARE_SIZE + (SQUARE_SIZE*i), SQUARE_SIZE + (SQUARE_SIZE*j), SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(BACKGROUND, BLACK, rect, 1)
            window.blit(BACKGROUND, (0,0))
        pygame.display.update()
        
    def update_visuals(self, new_stone=None):
        """Updates the groups of the stones on the board when a new stone is placed.

        Args:
            new_stone (Stone, optional): The new stone being placed. Defaults to None.
        """
        # updating the group of the new stone
        if new_stone:
            new_stone.group.update_groups()
            for group in self.groups:
                if group != new_stone.group:
                    group.update_groups()
        self.update_points()
