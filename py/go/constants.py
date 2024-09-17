import pygame

"""
This is a constants file that I used to store constants that I use frequently throughout the program.
"""

#window sizes
WIDTH, HEIGHT = 900, 900
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
#NOTE: 10 rows and cols to centre the grid, ignore first and last col
ROWS, COLS = 10, 10 

SQUARE_SIZE = 90

#colours
WHITE = (255,255,255)
BLACK = (0,0,0)
BROWN = (133,94,66)

#images
BACKGROUND = pygame.image.load('py/assets/background.png').convert()
WHITE_STONE = pygame.image.load('py/assets/white.png')
BLACK_STONE = pygame.image.load('py/assets/black.png')