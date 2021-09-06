# # def multiple_values(arg1, arg2, arg3):
# #     return arg1 * arg2 * arg3
# #
# # print(multiple_values(2, 3, 9))
#
# # my_list = [1, 2, 3, 4, 5,]
# # x,y,*z = my_list
# # print(x,y,z)
#
# # def piramid(x):
# #     for i in range(1, x+1):
# #         print('*' * i)
# # piramid(5)
#
# my_list = [1, 3, 5, 4, 2, 6]
#
#
# def min_max(x):
#    return min(x), max(x)
#
#
# def if_sorting(x):
#     if x == sorted(x):
#         return True
#     else:
#         return False
#
#
# def factorial(x):
#     result = 1
#     for i in range(1, x + 1):
#         result *= i
#     return result
#
#
# def tram(ticket, month):
#     return int(month/ticket)
#
#
# def letter_in_string(my_str, letter):
#     x = 0
#     for i in my_str:
#         if i == letter:
#             x += 1
#     return x


def players(count):
    players = {}
    for player in range(1, count + 1):
        print(f'''Введіть ім'я гравця {player}: ''')
        name = input()
        loop = True
        while loop:
            variants = input(f'{name} введіть одне з трьох  "Камінь, Ножниці, Папір"').lower()
            if variants not in chy_va_chi:
                continue
            else:
                players.update({name: variants})
                loop = False
    return players


def the_game(dict_players):
    variants = list(dict_players.values())
    vinner = ''
    if 'камінь' in variants and 'ножниці' in variants and 'папір'in variants:
        print('Нічия')
    elif 'камінь' not in variants and 'ножниці' not in variants:
        print('Нічия')
        return
    elif 'камінь' not in variants and 'папір' not in variants:
        print('Нічия')
        return
    elif 'папір' not in variants and 'ножниці' not in variants:
        print('Нічия')
        return
    else:
        if 'камінь' in variants and 'ножниці' in variants:
            vinner = 'камінь'
        elif 'камінь' in variants and 'папір' in variants:
            vinner = 'папір'
        elif 'папір' in variants and 'ножниці' in variants:
            vinner = 'ножниці'
    for player, variant in dict_players.items():
        if variant == vinner:
            print(f'Гравець - {player} переміг')
        else:
            print(f'Гравець - {player} програв')


# print(min_max(my_list))
# print(if_sorting(my_list))
# print(factorial(6))
# print(tram(2, 100))
# print(letter_in_string('coroc', 'o'))

chy_va_chi = ('камінь', 'ножниці', 'папір')
print('Введіть к-сть гравців: ')
players = players(int(input()),)
the_game(players)

