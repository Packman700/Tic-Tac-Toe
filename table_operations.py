import math
from colorama import Fore, Style

o = '{}o{}'.format(Fore.BLUE, Style.RESET_ALL)
x = '{}x{}'.format(Fore.RED, Style.RESET_ALL)

def create_2d_table_with_index():
    '''
    This create 3x3 list with index from 1 to 9
    '''
    table = []
    for i in range(3):
        table.append([])

    for line,index in zip(table, range(0, 9, 3)):
        for index2 in range(1, 4):
            line.append(f"{Fore.LIGHTBLACK_EX}{index+index2}{Style.RESET_ALL}")
    return table


def print_table(table):
    print('  {} | {} | {} \n'.format(table[0][0],table[0][1],table[0][2]),
          '----------- \n'
          '  {} | {} | {} \n'.format(table[1][0],table[1][1],table[1][2]),
          '----------- \n'
          '  {} | {} | {} \n'.format(table[2][0],table[2][1],table[2][2]),
)


def update_table(table,chose,symbol):
    '''
    this give value to table and validate data
    :param table: this is all data
    :param chose: number from 1 to 9
    :param shape: true=='o' or false=='x'
    :return:
    '''

    if table[(math.ceil(chose/3))-1][(chose % 3)-1] == x or table[(math.ceil(chose/3))-1][(chose % 3)-1] == o:
        return False
    else:
        table[(math.ceil(chose / 3)) - 1][(chose % 3) - 1] = symbol
        return table

# x = create_2d_table_with_index()
# x = update_table(x,1,False)
# print_table(x)
# x = update_table(x,1,True)
# print_table(x)