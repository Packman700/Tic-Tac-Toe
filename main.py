from table_operations import *
from procedures import *
from recognition_of_victory import *
from colorama import Fore, Style
from bot_turn import *
import os

print('Welcome in tic tac toe\n')

while True:
    try:
        difficulty_level = int(input('Chose difficulty level:\n'
                                     f'{Fore.GREEN}1.Easy {Style.RESET_ALL}\n'
                                     f'{Fore.YELLOW}2.Medium {Style.RESET_ALL}\n'
                                     f'{Fore.RED}3.Hard {Style.RESET_ALL}\n'
                                     f'Your chose: '))
        # os.system('cls')
        if difficulty_level > 3:
            print('Enter number from 1 to 3')
            continue
    except:
        print('Enter number!')
        continue
    break

while True:
    win_lose = False
    human_turn = True
    table = create_2d_table_with_index()
    for turn in range(9):
        if turn % 2: symbol='{}o{}'.format(Fore.BLUE, Style.RESET_ALL)
        else: symbol='{}x{}'.format(Fore.RED, Style.RESET_ALL)

        print_table(table)
        if human_turn:
            table = chose_field(table, symbol)
            human_turn = False

        else:  # bot tour
            # table = chose_field(table, symbol)
            table = bot_chose_turn(table, symbol, difficulty_level)
            human_turn = True

        if recognition_of_victory(table):
            win_lose = True
            print('Test')
            break

        # os.system('cls')

    else:
        print_table(table)
        print('Draw')

    if win_lose == True:
        print_table(table)
        print('{} WIN'.format(symbol))

    if input('Do you want play again Y|N').lower() == 'y':
        continue
    else:
        break

print('Goodbay')