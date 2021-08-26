print('   Завдання 1')
my_tuple = ('abc', 25, '32')
for i in my_tuple:
    if isinstance(i, int):
        print(f'{i} - це число')
print('')
print('   Завдання 2')

my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)
print('')
print('   Завдання 3')
x = ['d', 'a', 'w', 'i', 's', 'd', 'a']
print(set(x))

print('')
print('   Завдання 4')
my_list2 = [1, 5, -6, 8, 0, -2, -4]
del_items = my_list2.copy()
list_sum = 0
for i in my_list2:
    if i <= 0:
        print(f'''Знайдено від`ємне число - {i}''')
        del_items.remove(i)
    else:
        list_sum = list_sum + i
print(del_items)
print(f'Сума всіх додатніх чисел - {list_sum}')

print('')
print('   Завдання 5')
my_dict = {0: 'London',
           1: 'New-York',
           2: 'Berlin'}
print(f'Дано словник - {my_dict}')
print(f'Значення - {list(my_dict.values())}')
print(f'Ключі - {list(my_dict.keys())}')
print('')
new_dict = {value: key for key, value in my_dict.items()}
print(f'Ключі та значення міняємо місцями - {new_dict}')


