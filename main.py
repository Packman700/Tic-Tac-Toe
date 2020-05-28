from table_operations import *
from procedures import *
from recognition_of_victory import *
from colorama import Fore, Style
from bot_turn import *
import os

print('Welcome in tic tac toe\n')


game_mode = chose_mode()  # Chose mode interface
if game_mode != 1:
    difficulty_level = chose_level(game_mode)  # Chose level interface
human_turn = True
new_game = True
win_lose = False
round_number = 0

while True:
    if new_game:  # This decides who start current game
        round_number += 1
        human_turn = who_start(game_mode, round_number, human_turn)
    win_lose = False

    table = create_2d_table_with_index()
    for turn in range(9):  # Game loop
        if turn % 2:  # Generate current symbol
            symbol='{}o{}'.format(Fore.BLUE, Style.RESET_ALL)
        else:
            symbol='{}x{}'.format(Fore.RED, Style.RESET_ALL)

        print_table(table)  # Show game board

        if human_turn:  # Human move
            table = chose_field(table, symbol)
            if human_turn and game_mode != 1:
                human_turn = False
            else:
                human_turn = True

        else:  # Bot move
            table = bot_chose_turn(table, symbol, difficulty_level)
            if human_turn and game_mode != 1:
                human_turn = False
            else:
                human_turn = True

        if recognition_of_victory(table):  # Win recognize
            win_lose = True
            print('Test')
            break

        # os.system('cls')

    else:  # This show if nobody win
        print_table(table)
        print('Draw')

    if win_lose == True:  # This show who win
        print_table(table)
        print('{} WIN'.format(symbol))

    if input('Do you want play again Y|N: ').lower() == 'y':
        new_game = True
        continue
    else:
        break

print('Goodbay')