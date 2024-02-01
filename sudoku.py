import pygame
import sys
from sudoku_generator import *
import copy


pygame.init()

# Set up the display
width, height = 630, 700 # 70 each box
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Main Menu')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255,127,127)
GREEN = (90, 200, 50)
ORANGE = (255, 180, 0)
DRed = (222, 34, 15)

# Fonts
main_menu_font = pygame.font.SysFont('Chalkboard', 40)
button_font = pygame.font.SysFont('Arial', 25)
number_font = pygame.font.SysFont('Arial', 35)
shadow_font = pygame.font.SysFont('Arial', 25)


#Board Function
class Board:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.screen = screen


    def draw(self, board, selected_cell):
        global sudoku_board, shadow_board, running, x ,y, reseted_board, sudoku_board_dupe
        for i in range(1, 4):
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * 210), (self.width, i * 210), 8)
        for i in range(1, 4):
            pygame.draw.line(self.screen, (0, 0, 0), (i * 210, 0), (i * 210, 630), 8)
        for i in range(1, 9):
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * 70), (self.width, i * 70), 3)
        for i in range(1, 9):
            pygame.draw.line(self.screen, (0, 0, 0), (i * 70, 0), (i * 70, 630), 3)
        if selected_cell != None and selected_cell[0] < 9:
            red_rect = pygame.Rect(selected_cell[1]*70,selected_cell[0]*70, 70, 70)
            pygame.draw.rect(screen, RED, red_rect, 5)

        for i in range(9):
            for j in range(9):
                rect = pygame.Rect(j * 70, i * 70, 70, 70)
                if board[i][j] != 0:
                    text = number_font.render(str(board[i][j]), True, BLACK)
                    self.screen.blit(text, rect.move(70//3, 70//4))
                if shadow_board[i][j] != 0:
                    text = shadow_font.render(str(shadow_board[i][j]), True, RED)
                    self.screen.blit(text, rect.move(70//9, 70//12))

        game_on_font = pygame.font.SysFont('Chalkboard', 20)

        reset_button = pygame.Rect(70, 650, 70, 30)
        pygame.draw.rect(screen, BLACK, reset_button)
        text_surface = game_on_font.render("Reset", True, WHITE)
        text_rect = text_surface.get_rect(center=(reset_button.centerx, reset_button.centery))
        screen.blit(text_surface, text_rect)

        restart_button = pygame.Rect(280, 650, 70, 30)
        pygame.draw.rect(screen, BLACK, restart_button)
        text_surface = game_on_font.render("Restart", True, WHITE)
        text_rect = text_surface.get_rect(center=(restart_button.centerx, restart_button.centery))
        screen.blit(text_surface, text_rect)

        exit_button = pygame.Rect(490, 650, 70, 30)
        pygame.draw.rect(screen, BLACK, exit_button)
        text_surface = game_on_font.render("Exit", True, WHITE)
        text_rect = text_surface.get_rect(center=(exit_button.centerx, exit_button.centery))
        screen.blit(text_surface, text_rect)

        if reset_button.collidepoint(x, y):
            sudoku_board = copy.deepcopy(reseted_board)
            shadow_board = [[0 for _ in range(9)] for _ in range(9)]
        pygame.display.flip()

        if restart_button.collidepoint(x,y):
            x,y = 0,0
            sudoku_board = generate_sudoku(9, draw_menu())
            sudoku_board_dupe = copy.deepcopy(sudoku_board)
            shadow_board = [[0 for _ in range(9)] for _ in range(9)]
            reseted_board = copy.deepcopy(sudoku_board)



        if exit_button.collidepoint(x,y):
            running = False

#Initial starting screen
def draw_menu():
    screen.fill(WHITE)
    main_menu_font = pygame.font.SysFont('Chalkboard', 40)
    text_surface = main_menu_font.render("Sudoku - Main Menu", True, BLACK)
    text_rect = text_surface.get_rect(center=(315,200))
    screen.blit(text_surface, text_rect)

    easy_button_border = pygame.Rect(width // 2-115, height // 2 -25, 230, 50)
    pygame.draw.rect(screen, GREEN, easy_button_border, 5)

    easy_button = pygame.Rect(width // 2-100, height // 2 -25, 200, 50)
    pygame.draw.rect(screen,BLACK, easy_button)
    text_surface = main_menu_font.render("Easy", True, WHITE)
    text_rect = text_surface.get_rect(center=(easy_button.centerx,easy_button.centery))
    screen.blit(text_surface, text_rect)

    medium_button_border = pygame.Rect(width // 2 - 115, height // 2 + 50, 230, 50)
    pygame.draw.rect(screen, ORANGE, medium_button_border, 5)

    medium_button = pygame.Rect(width // 2 - 100, height // 2 + 50, 200, 50)
    pygame.draw.rect(screen, BLACK, medium_button)
    text_surface = main_menu_font.render("Medium", True, WHITE)
    text_rect = text_surface.get_rect(center=(medium_button.centerx, medium_button.centery))
    screen.blit(text_surface, text_rect)

    hard_button_border = pygame.Rect(width // 2 - 115, height // 2 + 125, 230, 50)
    pygame.draw.rect(screen, RED, hard_button_border, 5)

    hard_button = pygame.Rect(width // 2 - 100, height // 2 + 125, 200, 50)
    pygame.draw.rect(screen, BLACK, hard_button)
    text_surface = main_menu_font.render("Hard", True, WHITE)
    text_rect = text_surface.get_rect(center=(hard_button.centerx, hard_button.centery))
    screen.blit(text_surface, text_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if easy_button.collidepoint(x, y):
                    return 30
                elif medium_button.collidepoint(x, y):
                    return 40
                elif hard_button.collidepoint(x, y):
                    return 50
            pygame.display.update()



def end_screen(text):
    global x, y, running, sudoku_board_dupe, shadow_board, reseted_board, sudoku_board
    screen.fill(WHITE)
    main_menu_font = pygame.font.SysFont('Chalkboard', 40)
    text_surface = main_menu_font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(315, 200))
    screen.blit(text_surface, text_rect)

    if text == "Game Won!":
        exit_button = pygame.Rect(width // 2 - 100, height // 2 - 25, 200, 50)
        pygame.draw.rect(screen, BLACK, exit_button)
        text_surface = main_menu_font.render("Exit", True, WHITE)
        text_rect = text_surface.get_rect(center=(exit_button.centerx, exit_button.centery))
        screen.blit(text_surface, text_rect)
        if exit_button.collidepoint(x,y):
            running = False
        x, y = 0,0

    if text == "Game Over :(":
        restart_button = pygame.Rect(width // 2 - 100, height // 2 - 25, 200, 50)
        pygame.draw.rect(screen, BLACK, restart_button)
        text_surface = main_menu_font.render("Restart", True, WHITE)
        text_rect = text_surface.get_rect(center=(restart_button.centerx, restart_button.centery))
        screen.blit(text_surface, text_rect)
        if restart_button.collidepoint(x, y):
            sudoku_board = generate_sudoku(9, draw_menu())

            sudoku_board_dupe = copy.deepcopy(sudoku_board)
            shadow_board = [[0 for _ in range(9)] for _ in range(9)]
            reseted_board = copy.deepcopy(sudoku_board)
        x, y = 0, 0
    pygame.display.flip()


def check_if_wins():
    for i in range(9):
        for j in range(9):
            if sudoku_board[i][j] == 0:
                return "Not Finished"
    total_count = 0
    total_needed = 810
    for i in sudoku_board:
        for j in range(9):
            total_count += i[j]
    for i in range(9):
        for j in range(9):
            total_count += sudoku_board[j][i]
    if total_needed == total_count:
        return True
    else:
        return False




board = Board(630,700, screen)

sudoku_board = generate_sudoku(9, draw_menu())
sudoku_board_dupe = copy.deepcopy(sudoku_board)
shadow_board = [[0 for _ in range(9)] for _ in range(9)]
reseted_board = copy.deepcopy(sudoku_board)

x,y = 0, 0

i,j = (0,0)


running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            x, y = pygame.mouse.get_pos()
            i,j = (y//70,x//70)



 
        if event.type == pygame.KEYDOWN and (i < 9):
            if event.key == pygame.K_RETURN:
                if shadow_board[i][j] != 0:
                    sudoku_board[i][j] = shadow_board[i][j]
                    shadow_board[i][j] = 0
            if event.key == pygame.K_1:
                if sudoku_board_dupe[i][j] == 0:
                    shadow_board[i][j] = 1
            if event.key == pygame.K_2:
                if sudoku_board_dupe[i][j] == 0:
                    shadow_board[i][j] = 2
            if event.key == pygame.K_3:
                if sudoku_board_dupe[i][j] == 0:
                    shadow_board[i][j] = 3
            if event.key == pygame.K_4:
                if sudoku_board_dupe[i][j] == 0:
                    shadow_board[i][j] = 4
            if event.key == pygame.K_5:
                if sudoku_board_dupe[i][j] == 0:
                    shadow_board[i][j] = 5
            if event.key == pygame.K_6:
                if sudoku_board_dupe[i][j] == 0:
                    shadow_board[i][j] = 6
            if event.key == pygame.K_7:
                if sudoku_board_dupe[i][j] == 0:
                    shadow_board[i][j] = 7
            if event.key == pygame.K_8:
                if sudoku_board_dupe[i][j] == 0:
                    shadow_board[i][j] = 8
            if event.key == pygame.K_9:
                if sudoku_board_dupe[i][j] == 0:
                    shadow_board[i][j] = 9



            if event.key == pygame.K_DOWN:
                i += 1
            if event.key == pygame.K_UP:
                i -= 1
            if event.key == pygame.K_LEFT:
                j -= 1
            if event.key == pygame.K_RIGHT:
                j += 1
            if j < 0:
                j += 1
            if i < 0:
                i += 1
            if i > 8:
                i -= 1
            if j > 8:
                j -= 1

        pygame.display.update()
        screen.fill(WHITE)


        if check_if_wins() == "Not Finished":
            board.draw(sudoku_board, (i, j))
            continue
        elif check_if_wins() == True:
            end_screen("Game Won!")
        elif check_if_wins() == False:
            end_screen("Game Over :(")

    pygame.display.flip()

pygame.quit()
sys.exit()
