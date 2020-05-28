from table_operations import *

def chose_field(table, symbol, chose = None):
    """
    There user chose field to put 'x' or 'o'
    :param table: this is all data
    :param shape: true=='o' or false=='x'
    :param chose: index can be put usingstandard function input
    :return:
    """
    while True:
        if chose is None:
            try:
                chose = int(input('Enter index: '))
                if not 1 <= chose <= 9:
                    print('Enter must number from 1 to 9!')
                    chose = None
                    continue
            except:
                print('You entered wrong value')
                chose = None
                continue

        table_copy = update_table(table, chose, symbol)
        if table_copy == False:
            print('Field is occupied')
            chose = None
            continue
        else:
            table = table_copy
            break
    print()
    return table


def who_start(game_mode,round_number,human_turn):
    if game_mode == 1:
        return human_turn
    elif game_mode == 2:
        if round_number % 2 == 1:
            return True
        else:
            return False
    elif game_mode == 3:
        return True
    elif game_mode == 4:
        return False


def chose_mode():
    while True:
        try:
            game_mode = int(input('Chose game mode:\n'
                                  f'1.Play with other human\n'
                                  f'2.Play with bot\n'
                                  f'3.Play with bot (attack mode)\n'
                                  f'4.Play with bot (defence mode)\n'
                                  f'Your chose: '))
            if not 1 <= game_mode <= 4:
                print('Enter number from 1 to 4')
                continue
        except:
            print('Enter number!')
            continue
        break
    return game_mode


def chose_level(game_mode):
    if game_mode != 1:
        while True:
            try:
                difficulty_level = int(input('Chose difficulty level:\n'
                                             f'{Fore.GREEN}1.Easy {Style.RESET_ALL}\n'
                                             f'{Fore.YELLOW}2.Medium {Style.RESET_ALL}\n'
                                             f'{Fore.RED}3.Hard {Style.RESET_ALL}\n'
                                             f'{Fore.WHITE}4.Nightmare {Style.RESET_ALL}\n'
                                             f'Your chose: '))
                # os.system('cls')
                if not 1 <= difficulty_level <= 4:
                    print('Enter number from 1 to 4')
                    continue
            except:
                print('Enter number!')
                continue
            break
    return difficulty_level