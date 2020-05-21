from table_operations import *


def chose_field(table,symbol):
    """
    There user chose field to put 'x' or 'o'
    :param table: this is all data
    :param shape: true=='o' or false=='x'
    :return:
    """
    while True:
        try:
            chose = int(input('Enter index: '))
        except:
            print('You entered wrong value')
            continue

        table_copy = update_table(table, chose, symbol)
        if table_copy == False:
            print('Field is occupied')
            continue
        else:
            table = table_copy
            break
    print()
    return table