from go.stone import Stone
from .constants import WINDOW, BACKGROUND, BLACK, BLACK_STONE, WHITE_STONE
import pygame

class StoneView(Stone):
    """This class defines the front-end representation of the Stone model.

    Args:
        Stone (Stone): The stone class that contains the model
    """
    
    def __init__(self, board, coord, colour, blit_coords=None):
        """Inherits the stone model and translates the model coordinates
        to coordinates to print on the screen, as well as running the draw
        method upon creation of a new stone.

        Args:
            board (Board): The board a stone is associated with
            coord (Tuple): The stone's position in the model
            colour (Bool): Either black or white
            blit_coords (Tuple, optional): A transformation of the coord to locate the stone on screen. Defaults to None.
        """
        super().__init__(board, coord, colour)
        self.blit_coords = self.coord[0] * 90, self.coord[1] * 90
        self.draw()
        
    def draw(self):
        """Draws the stone onto the window.
        """
        WINDOW.blit(self.get_image(), self.get_image().get_rect(center=self.blit_coords))
        pygame.display.update()
        
    def delete(self):
        """Deletes a stone from the front-end, then calls to delete the stone in the model.
        """
        rect = pygame.Rect((self.blit_coords[0] - 43, self.blit_coords[1] - 43), (86,86))
        WINDOW.blit(BACKGROUND, (self.blit_coords[0] - 43, self.blit_coords[1] - 43), rect)
        pygame.display.update()
        super().delete()
        
    def get_image(self):
        """Returns the image associated with the colour of the stone.

        Returns:
            Image: the image of the stone
        """
        if self.colour == BLACK:
            return BLACK_STONE
        else:
            return WHITE_STONE