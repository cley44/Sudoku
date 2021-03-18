import pygame
import random
import time


pygame.init()

WIDTH, HEIGHT = 450, 500

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
    print("SUDOKU: \n",board[0])        
    print("\n",board[1])
    print("\n",board[2])
    print("\n",board[3])
    print("\n",board[4])
    print("\n",board[5])
    print("\n",board[6])
    print("\n",board[7])
    print("\n",board[8])
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

def make_full_board():
    
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


def make_board():

    for row in range(9):
        nbr_alea = random.randint(0,8)
        board[row][nbr_alea] = " "
        nbr_alea = random.randint(0,8)
        board[row][nbr_alea] = " "

    for column in range(9):
        nbr_alea = random.randint(0,8)
        board[nbr_alea][column] = " "
        nbr_alea = random.randint(0,8)
        board[nbr_alea][column] = " "

def draw_button():

    posy = 30
    button_height = HEIGHT-50/2-35/2

    for nombre in range(10):
        pygame.draw.rect(WIN, BLACK, [posy, button_height, 35,35],2)
        posy += 40
    

    draw_button_nombre(button_height)

    pygame.display.update()

def draw_button_nombre(button_height):

    posy = 44

    for nombre in range(1,10):
        text = font.render(str(nombre), 1, BLACK)
        WIN.blit(text, (posy, button_height+10))
        posy += 40

    pygame.draw.line(WIN, BLACK, (390, button_height),(posy+21,button_height+35),2)
    pygame.draw.line(WIN, BLACK, (424, button_height),(posy-14,button_height+34),2)
    

def draw_waiting():
    WIN.fill(WHITE)
    text = font.render("LOADING...",1,BLACK)
    text_width = text.get_width()
    text_height = text.get_height()
    WIN.blit(text, (WIDTH/2-text_width/2,HEIGHT/2-text_height/2))
    text = font.render("mading the sudoku",1,BLACK)
    text_width = text.get_width()
    text_height = text.get_height()
    WIN.blit(text, (WIDTH/2-text_width/2,HEIGHT/2-text_height/2+20))

    pygame.display.update()

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
            text = font.render(str(board[row][column]), 1, BLACK)
            text_width = text.get_width()
            text_height = text.get_height()
            WIN.blit(text, (pos_numero[column]/2-text_width/2, pos_numero[row]/2-text_height/2))


def draw_window():

    WIN.fill(WHITE)

    draw_board()
    draw_button()

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    button_height = HEIGHT-50/2-35/2
    while run:
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Boutton 1
                if 30 < mouse[0] < 30+35 and button_height < mouse[1] < button_height + 35:
                    nbr_selec = "1"
                # Boutton 2
                if 70 < mouse[0] < 70+35 and button_height < mouse[1] < button_height + 35:
                    nbr_selec = "2"
                # Boutton 3
                if 110 < mouse[0] < 110+35 and button_height < mouse[1] < button_height + 35:
                    nbr_selec = "3"
                # Boutton 4
                if 150 < mouse[0] < 150+35 and button_height < mouse[1] < button_height + 35:
                    nbr_selec = "4"
                # Boutton 5
                if 190 < mouse[0] < 190+35 and button_height < mouse[1] < button_height + 35:
                    nbr_selec = "5"
                # Boutton 6
                if 230 < mouse[0] < 230+35 and button_height < mouse[1] < button_height + 35:
                    nbr_selec = "6"
                # Boutton 7
                if 270 < mouse[0] < 270+35 and button_height < mouse[1] < button_height + 35:
                    nbr_selec = "7"
                # Boutton 8
                if 310 < mouse[0] < 310+35 and button_height < mouse[1] < button_height + 35:
                    nbr_selec = "8"
                # Boutton 9
                if 350 < mouse[0] < 350+35 and button_height < mouse[1] < button_height + 35:
                    nbr_selec = "9"
                # Boutton X
                if 390 < mouse[0] < 390+35 and button_height < mouse[1] < button_height + 35:
                    nbr_selec = " "
                pass


        draw_window()

    pygame.quit()


draw_waiting()
blank_board()
#make_full_board()
make_board()


if __name__ == "__main__":
    main()
