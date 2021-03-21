import pygame
import random
import time
import threading

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
pos_incorrect_color = []

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

    board_user = (board[0].copy(),board[1].copy(),board[2].copy(),board[3].copy(),board[4].copy(),board[5].copy(),board[6].copy(),board[7].copy(),board[8].copy())
    board_user_modif = (board[0].copy(),board[1].copy(),board[2].copy(),board[3].copy(),board[4].copy(),board[5].copy(),board[6].copy(),board[7].copy(),board[8].copy())

    print(board_user)

    for row in range(9):
        nbr_alea = random.randint(0,8)
        board_user[row][nbr_alea] = " "
        board_user_modif[row][nbr_alea] = " "
        nbr_alea = random.randint(0,8)
        board_user[row][nbr_alea] = " "
        board_user_modif[row][nbr_alea] = " "

    for column in range(9):
        nbr_alea = random.randint(0,8)
        board_user[nbr_alea][column] = " "
        board_user_modif[nbr_alea][column] = " "
        nbr_alea = random.randint(0,8)
        board_user[nbr_alea][column] = " "
        board_user_modif[nbr_alea][column] = " "

    return board_user,board_user_modif



def draw_button():

    posy = 10
    button_height = HEIGHT-50/2-35/2

    for nombre in range(11):
        pygame.draw.rect(WIN, BLACK, [posy, button_height, 35,35],2)
        posy += 40
    

    draw_button_nombre(button_height)

    pygame.display.update()

def draw_button_nombre(button_height):

    posy = 24

    for nombre in range(1,10):
        text = font.render(str(nombre), 1, BLACK)
        WIN.blit(text, (posy, button_height+10))
        posy += 40

    pygame.draw.line(WIN, BLACK, (370, button_height),(posy+21,button_height+35),2)
    pygame.draw.line(WIN, BLACK, (405, button_height),(posy-14,button_height+34),2)

    text = font.render("C", 1,BLACK)
    text_width = text.get_width()
    WIN.blit(text, (427 - text_width/2, button_height+10))
    

def draw_waiting():
    WIN.fill(WHITE)
    text = font.render("LOADING...",1,BLACK)
    text_width = text.get_width()
    text_height = text.get_height()
    WIN.blit(text, (WIDTH/2-text_width/2,HEIGHT/2-text_height/2))
    text = font.render("making the sudoku",1,BLACK)
    text_width = text.get_width()
    text_height = text.get_height()
    WIN.blit(text, (WIDTH/2-text_width/2,HEIGHT/2-text_height/2+20))

    pygame.display.update()

def draw_board(board_user_modif):
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
            text = font.render(str(board_user_modif[row][column]), 1, BLACK)
            text_width = text.get_width()
            text_height = text.get_height()
            WIN.blit(text, (pos_numero[column]/2-text_width/2, pos_numero[row]/2-text_height/2))


def draw_window(board_user_modif,nbr_selec):

    WIN.fill(WHITE)

    draw_board(board_user_modif)
    draw_button()
    draw_select_number(nbr_selec)

    pygame.display.update()


def put_number(mouse, nbr_selec,board_user,board_user_modif):

    row = 0
    column = 0

    for posy in range(0,HEIGHT-50,50):
        column = 0
        for posx in range(0,HEIGHT-50,50):

            if posx < mouse[0] < posx +50 and posy < mouse[1] < posy + 50:
                if board_user[row][column] == " ":
                    board_user_modif[row][column] = nbr_selec
        
            column +=1

        row += 1

def verify_win(board,board_user_modif):
    if board == board_user_modif:
        return True
    else:
        return False

def draw_win():

    WIN.fill(WHITE)
    text = font.render("YOU WON !",1,BLACK)
    text_width = text.get_width()
    text_height = text.get_height()
    WIN.blit(text, (WIDTH/2-text_width/2,HEIGHT/2-text_height/2))

    pygame.display.update()

def correct(board,board_user,board_user_modif):

    true_cell = 0

    for row in range(9):
        for column in range(9):
            if board_user[row][column] == " " and board_user_modif[row][column] != " ":
                if board_user_modif[row][column] == board[row][column]:
                    true_cell += 1
                else:
                    t = threading.Thread(None, draw_incorrect_color, None,(board_user_modif, row, column))
                    t.start()
                    board_user_modif[row][column] = board[row][column]
                    t.join()
                    time.sleep(0.01)

    print("Number of true cell: ", true_cell)

def draw_incorrect_color(board_user_modif, row, column):

    for numero in range(0, 450, 50):

        pos_incorrect_color.append(numero)

    for x in range(255,0,-1):
        WIN.fill(WHITE)
        draw_board(board_user_modif)

        s = pygame.Surface((50,50))
        s.set_alpha(x)
        s.fill((255,0,0))
        WIN.blit(s, (pos_incorrect_color[column],pos_incorrect_color[row]))
        pygame.display.update()
        time.sleep(0.001)

    pygame.display.update()

def draw_select_number(nbr_selec):


    posy = 10
    button_height = HEIGHT-50/2-35/2

    tab_posy = []

    for nombre in range(11):
        tab_posy.append(posy)
        posy += 40
    
    if nbr_selec == " ":
        nbr_selec = 10

    pygame.draw.rect(WIN, BLACK, [tab_posy[nbr_selec-1], button_height, 35,35],3)

    pygame.display.update()


def main(board_user, board_user_modif):
    clock = pygame.time.Clock()
    run = True
    button_height = HEIGHT-50/2-35/2
    nbr_selec = " "
    while run:
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Boutton 1
                if 10 < mouse[0] < 10+35 and button_height < mouse[1] < button_height + 35:
                    nbr_selec = 1
                    print("1")
                # Boutton 2
                if 50 < mouse[0] < 50+35 and button_height < mouse[1] < button_height + 35:
                    nbr_selec = 2
                    print("2")
                # Boutton 3
                if 90 < mouse[0] < 90+35 and button_height < mouse[1] < button_height + 35:
                    nbr_selec = 3
                    print("3")
                # Boutton 4
                if 130 < mouse[0] < 130+35 and button_height < mouse[1] < button_height + 35:
                    nbr_selec = 4
                    print("4")
                # Boutton 5
                if 170 < mouse[0] < 170+35 and button_height < mouse[1] < button_height + 35:
                    nbr_selec = 5
                    print("5")
                # Boutton 6
                if 210 < mouse[0] < 210+35 and button_height < mouse[1] < button_height + 35:
                    nbr_selec = 6
                    print("6")
                # Boutton 7
                if 250 < mouse[0] < 250+35 and button_height < mouse[1] < button_height + 35:
                    nbr_selec = 7
                    print("7")
                # Boutton 8
                if 290 < mouse[0] < 290+35 and button_height < mouse[1] < button_height + 35:
                    nbr_selec = 8
                    print("8")
                # Boutton 9
                if 330 < mouse[0] < 330+35 and button_height < mouse[1] < button_height + 35:
                    nbr_selec = 9
                    print("9")
                # Boutton X
                if 370 < mouse[0] < 370+35 and button_height < mouse[1] < button_height + 35:
                    nbr_selec = " "
                    print("espace")
                if 410 < mouse[0] < 410+35 and button_height < mouse[1] < button_height + 35:
                    correct(board,board_user, board_user_modif)
                    nbr_selec = 11
                pass
                
                
                put_number(mouse,nbr_selec,board_user, board_user_modif)

        if verify_win(board,board_user_modif):
            draw_win()
        else:
            draw_window(board_user_modif, nbr_selec)

    pygame.quit()


draw_waiting()
blank_board()
make_full_board()
board_user, board_user_modif = make_board()


if __name__ == "__main__":
    main(board_user, board_user_modif)
