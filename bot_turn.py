from recognition_of_victory import *
from procedures import *
import copy
import random


def bot_chose_turn(table,symbol,difficulty_level):
    o = '{}o{}'.format(Fore.BLUE, Style.RESET_ALL)
    x = '{}x{}'.format(Fore.RED, Style.RESET_ALL)
    adjacent_fields = {1: [2, 4],    2: [1, 3, 5],      3: [2, 6],
                           4: [1, 5, 7], 5: [1, 4, 6, 8],   6: [3, 5, 9],
                           7: [4, 8],    8: [5, 7, 9],      9: [6, 8]}

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

        score = defence_2exception_nightmare(empty_num_index, adjacent_fields)
        # Second+ exception
        if difficulty_level >= 4 and len(empty_num_index) == 6 and  score > 0:
            return chose_field(table, symbol, score)
        
        # First exception
        elif not(all(item in [1,9] for item in empty_num_index) or all(item in [3,7] for item in empty_num_index)) and difficulty_level >= 3 :
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
        x_index = []
        o_index = []
        # Create list with x and o index
        empty_num_index = []
        for num_line, line in enumerate(table):
            for num_cell, cell in enumerate(line):
                if 'o' in cell:
                    o_index.append(num_line * 3 + num_cell + 1)
                if 'x' in cell:
                    x_index.append(num_line * 3 + num_cell + 1)

        print(x_index)
        print(o_index)
        if difficulty_level >= 2:
            # Check bot can win in next move
            for index in empty_num_index:
                table_copy = copy.deepcopy(table)
                if recognition_of_victory(chose_field(table_copy, x, index)):
                    return chose_field(table, x, index)

            # Check you can win in next move
            for index in empty_num_index:
                table_copy = copy.deepcopy(table)
                if recognition_of_victory(chose_field(table_copy, o, index)):
                    return chose_field(table, x, index)

        # First tatic
        if len(empty_num_index)!=9 and difficulty_level >= 3:
            pass

        # Put 'o' on corner
        elif any(item in [1, 3, 7, 9] for item in empty_num_index) and difficulty_level >= 2:
            return chose_field(table, symbol, random.choice([index for index in [1, 3, 7, 9] if index in empty_num_index]))

        # Put 'o' on the middle
        if 5 in empty_num_index and difficulty_level >= 2:
            return chose_field(table, symbol, 5)

        # Put 'o' on side
        elif any(item in [2, 4, 6, 8] for item in empty_num_index) and difficulty_level >= 2:
            return chose_field(table, symbol, random.choice([index for index in [2, 4, 6, 8] if index in empty_num_index]))

    return table


def defence_2exception_nightmare(empty_num_index, adjacent_fields):
    #  Delete values from dic what not in empty list
    kay_to_del = []
    for key in adjacent_fields.keys():
        if key not in empty_num_index:
            kay_to_del.append(key)
    for kay in kay_to_del:
        del adjacent_fields[kay]

    for key in adjacent_fields:
        try:
            for value in adjacent_fields[kay]:
                if value in kay_to_del:
                    adjacent_fields[kay].remove(value)
        except:
            continue
    keys = adjacent_fields.keys()
    adjacent_fields_copy = copy.deepcopy(adjacent_fields)

    #delate all values what represent busy area
    kay_to_del2 = []
    for i in keys:
        for value in adjacent_fields[i]:
            if value in kay_to_del:
                adjacent_fields_copy[i].remove(value)
        if not len(adjacent_fields_copy[i]) == 1:
            kay_to_del2.append(i)

    for kay in kay_to_del2:
        del adjacent_fields_copy[kay]

    for out in adjacent_fields_copy.keys():
        if len(adjacent_fields_copy[out]) == 1:
            # print(adjacent_fields_copy[key])
            # print(key)
            # print(adjacent_fields_copy[key][0])
            try:
                if adjacent_fields_copy[adjacent_fields_copy[out][0]][0] == out:
                    if out in [1,3,7,9]:
                        return out
                        break
                    elif adjacent_fields_copy[out][0] in [1,3,7,9]:
                        return adjacent_fields_copy[out][0]
                        break
            except:
                pass
    return 0