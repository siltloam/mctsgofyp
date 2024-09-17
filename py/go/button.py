import pygame
from .constants import WINDOW, WHITE, BLACK

class Button():
    """Class to visually define buttons in the game.
    """

    def __init__(self, x, y, width, height, text):
        """Constructor for a button object

        Args:
            x (int): Horizontal positioning of button
            y (int): Vertical positioning of button
            width (int): Width of button
            height (int): Height of button
            text (String): Information inside the button
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.draw()

    def draw(self, outline=None):
        """Draw method for the button, placed on the window.

        Args:
            outline (pygame.Rect, optional): Potential outline for the button
        """
        pygame.font.init()
        if outline:
            pygame.draw.rect(WINDOW, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
        pygame.draw.rect(WINDOW, WHITE, (self.x, self.y, self.width, self.height), 0)

        font = pygame.font.SysFont(None, 20)
        text = font.render(self.text, 1, BLACK)
        WINDOW.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def hovering(self, pos):
        """Method to check whether the cursor is hovering over the button.

        Args:
            pos (Tuple): x and y coordinates of the cursor

        Returns:
            boolean: true/false
        """
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
    

