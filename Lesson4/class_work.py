# x = (40,)
# y = tuple((1, 2, 3, 4))
# print(x + y)
#
# my_tuple = ('a', 'b', 'c',)
# print(my_tuple.count('a'))
# print(my_tuple.index('a'))
#
# x = []
# y = list([1, 2, 3, 4])
# z = ['a']
# print(x + y)
#
# my_list = ['a', 'b', 'c']
# print(my_list.count('a'))
# print(my_list.index('a'))
# print(len(my_list))

# matrix = [[[1, 2, 3],[4, 5, 6], [7, 8, 9]],
#           [[10, 11, 12],[13, 14, 15], [16, 17, 18]],
#           [[19, 20, 21],[22, 23, 24], [25, 26, 27]]]
# print(matrix[2][2][2])

def len_x(e):
    return len(e)

# my_list = list()
# my_list.append(1)  # Добавлення елементу
# my_list.extend((1, 2, 3))  # Добавлення ітерабельного елементу
# # my_list.clear()  # Стирає всі елементи
# new_list = my_list.copy()
# my_list.insert(1, 'name')
# print(my_list)
# my_list.pop(2)
# my_list.remove(3)
# my_list.reverse()  # Виведе з кінця
# my_list = ['b', 'c', 'a']
# my_list.sort(key=len_x, reverse=True)  # сортує однотипні лісти.
# print(my_list.sort(key=len_x, reverse=True))


my_dict = {'key_1': 'abcd',
           'key_2': 'efg'}
# print(my_dict['key_2'])
# print(my_dict.get('key_1'))  # Вразі відсутності ключа поверне None
#
# my_dict['key_2'] = 'new value'
# print(my_dict['key_2'])
#
# print(list(my_dict.keys()))
# print(list(my_dict.values()))
# print(list(my_dict.items()))

# iterable = [22, 23, 24]
# y = "a"
# new_dict = dict.fromkeys(iterable, y)
# print(new_dict.items())
#
# iterable = range(1, 250)
# y = True
# new_dict = dict.fromkeys(iterable, y)
# print(new_dict.items())

# val = 'abcd'
#
# for key in my_dict:
#     if my_dict[key] == val:
#         print(key)

# ''' МНОЖИНИ '''
# x = set('spam')
# y = {'h', 'a', 'm'}

