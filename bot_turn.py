from recognition_of_victory import *
from procedures import *
import copy
import random


def bot_chose_turn(table,symbol,difficulty_level):
    o = '{}o{}'.format(Fore.BLUE, Style.RESET_ALL)
    x = '{}x{}'.format(Fore.RED, Style.RESET_ALL)

    # Create list with all blank values
    empty_num_index = []
    for num_line, line in enumerate(table):
        for num_cell, cell in enumerate(line):
            if 'o' not in cell and 'x' not in cell:
                empty_num_index.append(num_line*3 + num_cell + 1)

    if 'o' in symbol:  # Defence mode
        #  Easy level random chose
        if difficulty_level == 1:
            while True:
                index = random.randint(0,9)
                if index in empty_num_index:
                    return chose_field(table, o, index)

        if difficulty_level >= 2:
            # Check bot can win in next move
            for index in empty_num_index:
                table_copy = copy.deepcopy(table)
                if recognition_of_victory(chose_field(table_copy, o, index)):
                    return chose_field(table, o, index)

            # Check you can win in next move
            for index in empty_num_index:
                table_copy = copy.deepcopy(table)
                if recognition_of_victory(chose_field(table_copy, x, index)):
                    return chose_field(table, o, index)

        # Put 'o' on the middle
        if 5 in empty_num_index and difficulty_level >= 2:
            return chose_field(table, symbol, 5)

        # First exception
        elif not(all(item in [1,9] for item in empty_num_index) or all(item in [3,7] for item in empty_num_index)) and difficulty_level >= 3:
            return chose_field(table, symbol, random.choice([index for index in [2, 4, 6, 8] if index in empty_num_index]))

        # Second exception (1 variation)
        elif not(all(item in [6,7] for item in empty_num_index) or all(item in [1,8] for item in empty_num_index)) and difficulty_level >= 3:
            return chose_field(table, symbol, 9)

        # Second exception (2 variation)
        elif not(all(item in [2,9] for item in empty_num_index) or all(item in [3,4] for item in empty_num_index)) and difficulty_level >= 3:
            return chose_field(table, symbol, 1)

        # Put 'o' on corner
        elif any(item in [1, 3, 7, 9] for item in empty_num_index) and difficulty_level >= 2:
            return chose_field(table, symbol, random.choice([index for index in [1, 3, 7, 9] if index in empty_num_index]))

        # Put 'o' on side
        elif any(item in [2, 4, 6, 8] for item in empty_num_index) and difficulty_level >= 2:
            return chose_field(table, symbol, random.choice([index for index in [2, 4, 6, 8] if index in empty_num_index]))

    else: # Atack mode
        pass


    return table