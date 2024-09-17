import os
import pygame
import pygame_menu
import pyautogui
from go.constants import WINDOW, BLACK, WHITE
from go.button import Button
from mcts.mcts import MCTS
from go.board import Board
from go.stone import Stone
from go.stone_view import StoneView
from go.board_view import BoardView

def start_pvp():
    """Runs a player vs. player game of 9x9 Go.
    """
    run = True
    clock = pygame.time.Clock()
    board = BoardView()
    
    black_pass = Button(250, 10, 100, 40, "PASS (BLACK)")
    white_pass = Button(550, 10, 100, 40, "PASS (WHITE)")
    
    komi = float(pyautogui.prompt(text='Enter desired Komi!', title='Komi?', default='5.5'))
    board.white_points = komi

    while run:
        clock.tick(60)
        while board.game_over == False:
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if black_pass.hovering(pos):
                        board.pass_turn()
                    if white_pass.hovering(pos):
                        board.pass_turn()
                    if board.outline.collidepoint(event.pos) and event.button == 1:
                        x = int(round(((event.pos[0]) / 90), 0))
                        y = int(round(((event.pos[1]) / 90), 0))
                        added_stone = StoneView(board, (x,y), board.update_turn(), (x,y))
                        # print(added_stone.blit_coords)
                        # print(added_stone.coord)
                        board.update_visuals(added_stone)
                        # print(board.black_points, board.white_points)
                pygame.display.update()
        break
    pyautogui.alert(text="Game over! The score was to {b} to black and {w} to white!".format(b=board.black_points, w=board.white_points),
                    title='GAME OVER')
    pygame.quit()

def start_ai_game():
    """Runs a player vs. AI game of 9x9 Go.
    """
    run = True
    clock = pygame.time.Clock()
    board = BoardView()
    simulation_board = Board()
    tree = MCTS(0)
    
    black_pass = Button(400, 10, 100, 40, "PASS (PLAYER)")
    
    simulations = int(pyautogui.prompt(text='Enter desired simulation count', title='Simulations?', default='200'))
    if simulations == None:
        simulations == 200
    komi = float(pyautogui.prompt(text='Enter desired Komi!', title='Komi?', default='5.5'))
    board.white_points = komi
    simulation_board.white_points = komi
    while run:
        clock.tick(60)
        while board.game_over == False:
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if black_pass.hovering(pos):
                        board.pass_turn()
                        simulation_board.pass_turn()
                    if board.outline.collidepoint(event.pos) and event.button == 1:
                        x = int(round(((event.pos[0]) / 90), 0))
                        y = int(round(((event.pos[1]) / 90), 0))
                        added_stone = StoneView(board, (x,y), board.get_turn(), (x,y))
                        simulation_stone = Stone(simulation_board, (x,y), simulation_board.get_turn())
                        board.update_visuals(added_stone)
                        simulation_board.update_board(simulation_stone)
                        print("Player plays: ", (x,y))
                        play_node = tree.play(simulation_board, simulations)
                        board.turn += 1
                        simulation_board.turn += 1
                        x = int(round(((play_node.expansion_move[0]) / 90), 0))
                        y = int(round(((play_node.expansion_move[1]) / 90), 0))
                        new_stone = StoneView(board, play_node.expansion_move, board.update_turn(), (x,y))
                        simulation_stone = Stone(simulation_board, play_node.expansion_move, simulation_board.update_turn())
                        board.update_visuals(new_stone)
                        simulation_board.update_board(simulation_stone)
                        print("Computer plays:", play_node.expansion_move, " with:" , play_node.visit_count, " visits" )
                        print("Wins :", play_node.wins)
                        print("Sims : ", play_node.simulations)
                        print("Search depth :", tree.depth)
        pyautogui.alert(text="Game over! The score was to {b} to black and {w} to white!".format(b=board.black_points, w=board.white_points),
                title='GAME OVER')
        break
    pygame.quit()


def main():
    """Main driver for Go game.
    """
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption('9x9 Go')
    menu = pygame_menu.Menu('Welcome to 9x9 Go', 900, 900, theme=pygame_menu.themes.THEME_DARK)
    menu.add.button('Play PvP', start_pvp)
    menu.add.button('Play AI', start_ai_game)
    menu.add.button('Quit', pygame.quit)
    menu.mainloop(WINDOW)
    
pygame.init()
main()