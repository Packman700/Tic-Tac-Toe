from recognition_of_victory import *
from procedures import *
import copy
import random

global chosen_strategy


def bot_chose_turn(table,symbol,difficulty_level):
    o = '{}o{}'.format(Fore.BLUE, Style.RESET_ALL)
    x = '{}x{}'.format(Fore.RED, Style.RESET_ALL)
    adjacent_fields = {1: [2, 4],    2: [1, 3, 5],      3: [2, 6],
                           4: [1, 5, 7], 5: [1, 4, 6, 8],   6: [3, 5, 9],
                           7: [4, 8],    8: [5, 7, 9],      9: [6, 8]}

    # Create list with all blank values
    empty_field_num = []
    for num_line, line in enumerate(table):
        for num_cell, cell in enumerate(line):
            if 'o' not in cell and 'x' not in cell:
                empty_field_num.append(num_line*3 + num_cell + 1)

    if 'o' in symbol:  # Defence mode
        #  Easy level random chose
        if difficulty_level == 1:
            while True:
                index = random.randint(0,9)
                if index in empty_field_num:
                    return chose_field(table, o, index)

        if difficulty_level >= 2:
            # Check bot can win in next move
            for index in empty_field_num:
                table_copy = copy.deepcopy(table)
                if recognition_of_victory(chose_field(table_copy, o, index)):
                    return chose_field(table, o, index)

            # Check you can win in next move
            for index in empty_field_num:
                table_copy = copy.deepcopy(table)
                if recognition_of_victory(chose_field(table_copy, x, index)):
                    return chose_field(table, o, index)

        # Put 'o' on the middle
        if 5 in empty_field_num and difficulty_level >= 2:
            return chose_field(table, symbol, 5)

        score = defence_2exception_nightmare(empty_field_num, adjacent_fields)
        # Second+ exception
        if difficulty_level >= 4 and len(empty_field_num) == 6 and score > 0:
            return chose_field(table, symbol, score)

        elif 5 not in empty_field_num and len(empty_field_num) == 8:
            return chose_field(table, symbol, random.choice([index for index in [1, 3, 7, 9] if index in empty_field_num]))

        # First exception

        elif not(all(item in [1,9] for item in empty_field_num) or all(item in [3,7] for item in empty_field_num)) and difficulty_level >= 3 :
            return chose_field(table, symbol, random.choice([index for index in [2, 4, 6, 8] if index in empty_field_num]))

        # Second exception (1 variation)
        elif not(all(item in [6,7] for item in empty_field_num) or all(item in [1,8] for item in empty_field_num)) and difficulty_level >= 3:
            return chose_field(table, symbol, 9)

        # Second exception (2 variation)
        elif not(all(item in [2,9] for item in empty_field_num) or all(item in [3,4] for item in empty_field_num)) and difficulty_level >= 3:
            return chose_field(table, symbol, 1)

        # Put 'o' on corner
        elif any(item in [1, 3, 7, 9] for item in empty_field_num) and difficulty_level >= 2:
            return chose_field(table, symbol, random.choice([index for index in [1, 3, 7, 9] if index in empty_field_num]))

        # Put 'o' on side
        elif any(item in [2, 4, 6, 8] for item in empty_field_num) and difficulty_level >= 2:
            return chose_field(table, symbol, random.choice([index for index in [2, 4, 6, 8] if index in empty_field_num]))

    else:  # Atack mode
        # Create lists index with all x, o and empty values
        x_index = []
        for num_line, line in enumerate(table):
            for num_cell, cell in enumerate(line):
                if 'x' in cell:
                    x_index.append([num_line % 3, num_cell])
        o_index = []
        for num_line, line in enumerate(table):
            for num_cell, cell in enumerate(line):
                if 'o' in cell:
                    o_index.append([num_line % 3, num_cell])
        empty_field_index = []
        for num_line, line in enumerate(table):
            for num_cell, cell in enumerate(line):
                if 'o' not in cell and 'x' not in cell:
                    empty_field_index.append([num_line % 3, num_cell])

        # print(x_index)
        # print(o_index)
        # print(empty_field_index)

        if difficulty_level >= 2:
            # Check bot can win in next move
            for index in empty_field_num:
                table_copy = copy.deepcopy(table)
                if recognition_of_victory(chose_field(table_copy, x, index)):
                    return chose_field(table, x, index)

            # Check you can win in next move
            for index in empty_field_num:
                table_copy = copy.deepcopy(table)
                if recognition_of_victory(chose_field(table_copy, o, index)):
                    return chose_field(table, x, index)
        # All atacks
        if (len(x_index) == 1 or len(x_index) == 2) and difficulty_level >= 3:
            global chosen_strategy
            if len(x_index) == 1:
                # First.1 variant
                if o_index[0] == [1,1]:
                    return chose_field(table, x, index_to_number(shift_index_corner([2,2],x_index)[0]))
                # Second variant
                if o_index[0] in shift_index_corner([2,0],x_index):
                    return chose_field(table, x, index_to_number(shift_index_corner([2,2],x_index)[0]))
                # Third variant close side
                if o_index[0] in shift_index_side([1,0],x_index):
                    chosen_strategy = 3
                    return chose_field(table, x, 5)
                # Forth variant far side
                if o_index[0] in shift_index_corner([2,1],x_index):
                    chosen_strategy = 4
                    return chose_field(table, x, index_to_number(variant4(x_index,o_index)))
            if len(x_index) == 2:
                # First variant
                    # Doesn't need
                # Second variant
                    # Doesn't need
                # Third variant close side
                if chosen_strategy == 3:
                    return chose_field(table, x, index_to_number(variant3(x_index,o_index)))
                # Forth variant far side
                if chosen_strategy == 4:
                    return chose_field(table, x, 5)
        # Put 'x' on corner
        if any(item in [1, 3, 7, 9] for item in empty_field_num) and difficulty_level >= 2:
            return chose_field(table, symbol, random.choice([index for index in [1, 3, 7, 9] if index in empty_field_num]))

        # Put 'x' on the middle
        if 5 in empty_field_num and difficulty_level >= 2:
            return chose_field(table, symbol, 5)

        # Put 'x' on side
        elif any(item in [2, 4, 6, 8] for item in empty_field_num) and difficulty_level >= 2:
            return chose_field(table, symbol, random.choice([index for index in [2, 4, 6, 8] if index in empty_field_num]))
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


def variant4(x_index , o_index):
    results = shift_index_side([2,1],o_index)
    if results[0] != x_index[0]:
        return results[0]
    try:
        if results[1] != x_index[0]:
            return results[1]

    except:  # Because this function dont work in 2 cases
        if results[0] == [2,2]:
            return [0,2]
        else:
            return [0,0]


def variant3(x_index , o_index):
    results = shift_index_corner([0,1],x_index)
    if results == [[1,2],[2,1]]:  # Because this function dont work in 2 cases
        if [2,1] in o_index:
            return [1,0]
        else:
            return [2,1]
    if results[0] not in o_index:
        return results[0]
    if results[1] not in o_index:
        return results[1]


def shift_index_corner(shift, x_index):
    test1 = shift
    test2 = [shift[1],shift[0]]
    row = x_index[0][0]
    column = x_index[0][1]

    if 0 <= test1[0] + row <= 2 and 0 <= test1[1] + column <= 2:
        test_result1 = [test1[0] + row, test1[1] + column]
    elif 0 <= -test1[0] + row <= 2 and 0 <= test1[1] + column <= 2:
        test_result1 = [-test1[0] + row, test1[1] + column]
    elif 0 <= test1[0] + row <= 2 and 0 <= -test1[1] + column <= 2:
        test_result1 = [test1[0] + row, -test1[1] + column]
    elif 0 <= -test1[0] + row <= 2 and 0 <= -test1[1] + column <= 2:
        test_result1 = [-test1[0] + row, -test1[1] + column]
    else:
        test_result1 = None

    if 0 <= test2[0] + row <= 2 and 0 <= test2[1] + column <= 2:
        test_result2 = [test2[0] + row, test2[1] + column]
    elif 0 <= -test2[0] + row <= 2 and 0 <= test2[1] + column <= 2:
        test_result2 = [-test2[0] + row, test2[1] + column]
    elif 0 <= test2[0] + row <= 2 and 0 <= -test2[1] + column <= 2:
        test_result2 = [test2[0] + row, -test2[1] + column]
    elif 0 <= -test2[0] + row <= 2 and 0 <= -test2[1] + column <= 2:
        test_result2 = [-test2[0] + row, -test2[1] + column]
    else:
        test_result2 = None
    tests = []
    tests.append(test_result1)
    tests.append(test_result2)
    return tests


def shift_index_side(shift, o_index):
    test1 = shift
    test2 = [shift[1], shift[0]]
    row = o_index[0][0]
    column = o_index[0][1]
    test_result1 = []
    if 0 <= test1[0] + row <= 2 and 0 <= test1[1] + column <= 2:
        test_result1.append([test1[0] + row, test1[1] + column])
    if 0 <= -test1[0] + row <= 2 and 0 <= test1[1] + column <= 2:
        test_result1.append([-test1[0] + row, test1[1] + column])
    if 0 <= test1[0] + row <= 2 and 0 <= -test1[1] + column <= 2:
        test_result1.append([test1[0] + row, -test1[1] + column])
    if 0 <= -test1[0] + row <= 2 and 0 <= -test1[1] + column <= 2:
        test_result1.append([-test1[0] + row, -test1[1] + column])

    if 0 <= test2[0] + row <= 2 and 0 <= test2[1] + column <= 2:
        test_result1.append([test2[0] + row, test2[1] + column])
    elif 0 <= -test2[0] + row <= 2 and 0 <= test2[1] + column <= 2:
        test_result1.append([-test2[0] + row, test2[1] + column])
    elif 0 <= test2[0] + row <= 2 and 0 <= -test2[1] + column <= 2:
        test_result1.append([test2[0] + row, -test2[1] + column])
    elif 0 <= -test2[0] + row <= 2 and 0 <= -test2[1] + column <= 2:
        test_result1.append([-test2[0] + row, -test2[1] + column])

    return test_result1


def index_to_number(index):
    return index[0]*3+index[1]+1