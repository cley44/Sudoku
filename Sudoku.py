import pygame
import random
import time


pygame.init()

WIDTH, HEIGHT = 450, 450

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

FPS = 60

WHITE = 255, 255, 255
BLACK = 0, 0, 0
THICK = 2
BIG_THICK = 5

font = pygame.font.Font(None, 24)

board = ([5, 3, 4, 6, 7, 8, 9, 1, 2],
         [6, 7, 2, 1, 9, 5, 3, 4, 8],
         [1, 9, 8, 3, 4, 2, 5, 6, 7],
         [8, 5, 9, 7, 6, 1, 4, 2, 3],
         [4, 2, 6, 8, 5, 3, 7, 9, 1],
         [7, 1, 3, 9, 2, 4, 8, 5, 6],
         [9, 6, 1, 5, 3, 7, 2, 8, 4],
         [2, 8, 7, 4, 1, 9, 6, 3, 5],
         [3, 4, 5, 2, 8, 6, 1, 7, 9])

pos_numero = []


def blank_board():
    for row in range(9):
        for column in range(9):
            board[row][column] = " "

            
    print(board)


def choix_case(x, x1, y, y1):
    verif_case = []

    for row in range(x, x1):
        for column in range(y, y1):
            if verif_case.count(board[row][column]) == 0:
                if board[row][column] != " ":
                    verif_case.append(board[row][column])
            else:
                return False

    return True


def verif_case(row,collumn):

    if row <= 2:
        if collumn <= 2:
            return choix_case(0, 3, 0, 3)

        elif collumn > 2 and collumn <= 5:
            return choix_case(0, 3, 3, 6)

        elif collumn > 5:
            return choix_case(0, 3, 6, 9)

    elif row > 2 and row <= 5:
        if collumn <= 2:
            return choix_case(3, 6, 0, 3)

        elif collumn > 2 and collumn <= 5:
            return choix_case(3, 6, 3, 6)

        elif collumn > 5:
            return choix_case(3, 6, 6, 9)

    elif row > 5:
        if collumn <= 2:
            return choix_case(6, 9, 0, 3)

        elif collumn > 2 and collumn <= 5:
            return choix_case(6, 9, 3, 6)

        elif collumn > 5:
            return choix_case(6, 9, 6, 9)

    pass


def verif_column(collumn):

    verif_column = []

    for x in range(9):
        if verif_column.count(board[x][collumn]) == 0:
            if board[x][collumn] != " ":
                verif_column.append(board[x][collumn])
        else:
            return False

    return True


def verif_row(row):

    verif_row = []

    for x in range(9):
        if verif_row.count(board[row][x]) == 0:
            if board[row][x] != " ":
                verif_row.append(board[row][x])
        else:

            return False

    return True



def verif_all(row, collumn):
    print(board)
    if verif_column(collumn) and verif_row(row) and verif_case(row, collumn):
        return True
    else:
        return False

def trouver_case(row,column):

    compteur = 0

    while compteur < 15:
        nbr_alea = random.randint(1, 9)
        board[row][column] = nbr_alea
        compteur += 1
        if verif_all(row, column) == False:
            board[row][column] = " "
        else:
            return True

    return False

def make_board():

    case_depart = -1
    
    column = 0
    row = 0
    trouver = True

    while row < 9:
        column = 0
        while column < 9:
            
            trouver = trouver_case(row,column)
            while trouver == False:
                if column - 1 >= 0:
                    column -= 1
                elif column - 1 < 0:
                    column = 8
                    if row - 1 >= 0:
                        row -= 1
                case_depart = board[row][column]
                trouver = trouver_case(row,column)
                if board[row][column] == case_depart:
                    trouver = False
                    board[row][column] = " "
            
            column += 1
        row += 1


def draw_board():
    compteur = 0

    for posx in range(50, HEIGHT, 50):
        compteur += 1
        if compteur == 3:
            pygame.draw.line(WIN, BLACK, (0, posx), (HEIGHT, posx), BIG_THICK)
            compteur = 0
        else:
            pygame.draw.line(WIN, BLACK, (0, posx), (HEIGHT, posx), THICK)

    compteur = 0

    for posy in range(50, WIDTH, 50):
        compteur += 1
        if compteur == 3:
            pygame.draw.line(WIN, BLACK, (posy, 0), (posy, WIDTH), BIG_THICK)
            compteur = 0
        else:
            pygame.draw.line(WIN, BLACK, (posy, 0), (posy, WIDTH), THICK)

    for numero in range(50, 950, 100):

        pos_numero.append(numero)

    for row in range(9):
        for column in range(9):
            text = font.render(str(board[row][column]), 1, (0, 0, 0))
            text_width = text.get_width()
            text_height = text.get_height()
            WIN.blit(
                text, (pos_numero[column]/2-text_width/2, pos_numero[row]/2-text_height/2))


def draw_window():

    WIN.fill(WHITE)

    draw_board()

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


blank_board()
make_board()

if __name__ == "__main__":
    main()