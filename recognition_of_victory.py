def recognition_of_victory(table):
    '''
    This check all row, column and cross
    :param table:
    :return:
    '''
    for r in range(3):
        line_copy = []
        for c in range(3):
            line_copy.append(table[r][c])
        if line_copy[0] == line_copy[1] == line_copy[2]:
            return True

    for c in range(3):
        line_copy = []
        for r in range(3):
            line_copy.append(table[r][c])
        if line_copy[0] == line_copy[1] == line_copy[2]:
            return True

    if table[0][0] == table[1][1] == table[2][2] or table[2][0] == table[1][1] == table[0][2]:
        return True
    else:
        return False